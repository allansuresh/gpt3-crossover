from os import walk  # For getting names of input files
import json


# Function to remove action lines and descriptors from script - the stuff between brackets
# Takes string as argument
# Returns string
def remove_action(data):
	rem_data = ""

	# Since we update i inside the loop when we find an index of closing bracket, while works better than for, which doesn't allow updating as easily
	i = 0
	while i < len(data):
		if data[i] == "[":
			# Finding index of first closing bracket after the index of the opening bracket
			closing_index = data.find("]", i)
			i = closing_index + 1
			# Accounting for double spaces
			if i < len(data) and data[i] == " ":
				i = i + 1
			continue

		if data[i] == "(":
			closing_index = data.find(")", i)
			i = closing_index + 1
			if i < len(data) and data[i] == " ":
				i = i + 1
			continue
		
		# Append character if not between brackets to output
		rem_data = rem_data + data[i]

		i = i + 1

	return rem_data


# Function to split the data string into a list of the speaker-dialogue strings
# Takes string as argument
# Returns list
def split_lines(data):
	split = []

	line = ""

	# Since we update i inside the loop to remove successive \n, while works better than for, which doesn't allow updating as easily
	i = 0
	while i < len(data):
		if data[i] == "\n":
			# Line is over, append to the list
			split.append(line)
			line = ""
			# If script has consecutive \n between lines
			while i < len(data):
				if data[i] == "\n":
					i = i + 1
				else:
					break
			
			continue

		line = line + data[i]

		i = i + 1

	return split


# Function to convert list of lines to list of (prompt, response) tuple pairs
# Takes list of strings and names of people whose responses we want, as arguments
# Returns list of tuples
def convert_to_tuple(data, names):
	pairs = []

	# Variable to store the dialogue from previous loop iteration
	prev = ""

	for line in data:
		split_index = line.find(":")

		# speaker contains part of string until ":"
		speaker = line[:split_index+1].strip()
		response = line[split_index+1:].strip()

		# If the speaker is someone we want, prompt for their response is whatever was said last along with their name
		# The second conditional is for the case that the first speaker in a script is someone we want - there's no prompt there
		if speaker[:-1].lower() not in names.keys() or prev == "\n":
			# Store the response for the next loop
			prev = response
			continue

		prompt = prev + "\n" + names[speaker[:-1].lower()] + ":"
		prev = response

		# Making sure ":" is a unique suffix for prompts
		prompt = prompt.replace(":","") + ":"
		# Common string at the end to indicate to model where completion should end.
		response = response + "\n\n###\n\n"

		# Unicode characters are hard to deal with, so if they're in these, best to drop those lines
		if str.isascii(prompt) and str.isascii(response):
			pairs.append((prompt, response))

	return pairs


# Function to convert list of (speaker, dialogue) tuple pairs to JSON format
# Takes list of tuples as argument
# Returns list of dicts - JSON format
def convert_to_json(data):
	ret_list = []

	for pair in data:
		dict_pair = {}

		# Handling edge case where speaker isn't specified or dialogue is missing
		if pair[0] == "" or pair[1] == "":
			continue
		
		# First element of pair contains speaker
		dict_pair["prompt"] = pair[0]
		# Second element of pair contains dialogue, append whitespace to front according to OpenAI recommendations.
		# Refer: https://beta.openai.com/docs/guides/fine-tuning/preparing-your-dataset
		dict_pair["completion"] = " " + pair[1]

		ret_list.append(dict_pair)

	return ret_list


# Function to take raw data from input file and write cleaned JSONL formatted text to output file
# Takes names of input, output filenames, and names we care about as arguments
# No return
def pipeline(input_filename, output_filename, names):
	# Reading data from file
	with open(input_filename, "r", encoding="utf8") as input_file:
		data = input_file.read()
	#print(data)

	# Removing non-dialogue content from the script
	cleaned_data = remove_action(data)
	#print(cleaned_data)

	# Splitting cleaned data into list of strings containing speaker name and dialogue => one line
	lines = split_lines(cleaned_data)
	#print(lines)

	# Converting each line to a (speaker, dialogue) tuple
	pairs = convert_to_tuple(lines, names)
	#for i in pairs: print(i)

	# Converting each tuple to a JSON pair
	json_data = convert_to_json(pairs)
	#for i in json_data: print(i)


	# Writing data to output JSONL file
	with open(output_filename, "a") as output_file:
		for item in json_data:
			output_file.write(json.dumps(item) + "\n")

	'''
	with open(output_filename, "r") as output_file:
		for line in output_file:
			print(line)
	'''


def main():
	# Getting list of files in the Transcripts folder
	input_filenames = ["Transcripts/" + name for name in next(walk("Transcripts"), (None, None, []))[2]]
	output_filename = "finetune_data.jsonl"
	# Dict of different ways names appear in the scripts, mapped to the proper way we want them to appear
	names = {
			"tony stark":"Tony", "tony":"Tony", "iron man":"Tony", "steve rogers":"Steve", "steve":"Steve", "captain america":"Steve", "thor":"Thor", "loki": "Loki", 
			"scott":"Scott", "scott lang":"Scott", "peter parker":"Peter", "peter":"Peter", "natasha":"Black Widow", "natasha romanoff":"Black Widow", "banner":"Bruce Banner", 
			"fury":"Fury", "nick fury":"Fury", "clint":"Hawkeye", "barton":"Hawkeye", "wanda":"Wanda", "wanda maximoff":"Wanda", "vision":"Vision", 
			"carol danvers":"Captain Marvel", "carol":"Captain Marvel", "vers":"Captain Marvel", "thanos":"Thanos", "peter quill":"Star-Lord", "quill":"Star-Lord", 
			"doctor strange":"Doctor Strange", "stephen":"Doctor Strange", "stephen strange":"Doctor Strange", "dr. stephen strange":"Doctor Strange", 
			"arthur":"Aquaman", "bruce wayne":"Batman", "batman":"Batman", "superman":"Superman", "clark kent":"Superman", "diana":"Wonder Woman", 
			}

	for input_filename in input_filenames:
		pipeline(input_filename, output_filename, names)


if __name__ == "__main__":
	main()