import os
import sys
import openai

openai.api_key = os.getenv('OPENAI_KEY')


# Edit this variable to the name of the file containing finetuning data
filename = "finetune_data.jsonl"

# Edit this variable to the file ID of the uploaded finetuning data
file_id = "file-xsw6aLikSTVDmVhrYyq631dz"


# Function to upload file for finetuning
def upload_file(filename):
	openai.File.create(file=open(filename), purpose='fine-tune')

# Function to list files that have been uploaded - used to get file IDs
def list_files():
	print(openai.File.list())

# Function to delete files that have been uploaded
def delete_file(file_id):
	openai.File(file_id).delete()

# Function to create a finetuning job using the file_id passed as argument
def finetune(file_id):
	openai.FineTune.create(training_file=file_id)

# Function to list finetuning jobs
def finetune_list():
	print(openai.FineTune.list())


def main():
	# Taking arguments from command line
	n = len(sys.argv)

	# If program is called incorrectly, with no or more than one additional argument
	if n != 2:
		sys.exit("Try again with one argument.")

	if sys.argv[1] == "u":
		if input("Confirming: Do you want to upload the file {}? Y/N: ".format(filename)) == "Y":
			upload_file(filename)
	elif sys.argv[1] == "l":
		if input("Confirming: Do you want to list the uploaded files? Y/N: ") == "Y":
			list_files()
	elif sys.argv[1] == "d":
		if input("Confirming: Do you want to delete the file {}? Y/N: ".format(file_id)) == "Y":
			delete_file(file_id)
	elif sys.argv[1] == "f":
		if input("Confirming: Do you want to create a new finetuning job with the file {}? Y/N: ".format(file_id)) == "Y":
			finetune(file_id)
	elif sys.argv[1] == "fl":
		if input("Confirming: Do you want to list your finetuning jobs? Y/N: ") == "Y":
			finetune_list()
	else:
		sys.exit("Try one of \"u\", \"l\", \"d\", \"f\", or \"fl\" as the argument.")


if __name__ == '__main__':
	main()