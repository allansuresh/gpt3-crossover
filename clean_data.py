import json


# Function to remove action lines and descriptors from script - the stuff between square brackets
# Takes string as argument
# Returns string
def remove_action(data):
	rem_data = ""

	# Since we update i inside the loop when we find an index of closing square bracket, while works better than for, which doesn't allow updating as easily
	i = 0
	while i < len(data):
		if data[i] == "[":
			# Finding index of first closing bracket after the index of the opening bracket
			closing_index = data.find("]", i)
			# Skip to the index two steps after the closing square bracket, to account for double spaces
			i = closing_index + 2
			continue
		
		# Append character if not between square brackets to output
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


# Function to convert list of lines to list of (speaker, dialogue) tuple pairs
# Takes list of strings as argument
# Returns list of tuples
def convert_to_tuple(data):
	pairs = []

	for line in data:
		split_index = line.find(":")

		# speaker contains part of string until ":", including ":"
		speaker = line[:split_index+1].strip()
		dialogue = line[split_index+1:].strip()

		pairs.append((speaker, dialogue))

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
# Takes names of input and output filenames as arguments
# No return
def pipeline(input_filename, output_filename):
	# Reading data from file
	with open(input_filename, "r") as input_file:
		data = input_file.read()
	#print(data)

	# Removing non-dialogue content from the script
	cleaned_data = remove_action(data)
	#print(cleaned_data)

	# Splitting cleaned data into list of strings containing speaker name and dialogue => one line
	lines = split_lines(cleaned_data)
	#print(lines)

	# Converting each line to a (speaker, dialogue) tuple
	pairs = convert_to_tuple(lines)
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
	input_filename = "Transcripts/IM.txt"
	output_filename = "Transcripts/finetune_data.jsonl"

	pipeline(input_filename, output_filename)


if __name__ == "__main__":
	main()