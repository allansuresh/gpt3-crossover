import os
import sys
import openai

openai.api_key = os.getenv('OPENAI_KEY')


# Edit this variable to the name of the file containing finetuning data
filename = "finetune_data.jsonl"

# Edit this variable to the file ID of the uploaded finetuning data
file_id = "file-XGinujblHPwGLSztz8cPS8XY"


# Function to upload file for finetuning
def upload_file(filename):
	openai.File.create(file=open(filename), purpose='answers')

# Function to list files that have been uploaded - used to get file IDs
def list_files():
	openai.File.list()

# Function to create a finetuning job using the file_id passed as argument
def finetune(file_id):
	openai.FineTune.create(training_file=file_id)


def main():
	# Taking arguments from command line
	n = len(sys.argv)

	# If program is called incorrectly, with no or more than one additional argument
	if n != 2:
		sys.exit("Try again with one argument.")

	if sys.argv[1] == "u":
		upload_file(filename)
	elif sys.argv[1] == "l":
		list_files()
	elif sys.argv[1] == "f":
		finetune(file_id)
	else:
		sys.exit("Try one of \"u\", \"l\", or \"f\" as the argument.")


if __name__ == '__main__':
	main()