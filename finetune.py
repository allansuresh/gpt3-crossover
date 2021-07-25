import os
import sys
import openai

openai.api_key = os.getenv('OPENAI_KEY')


filename = "finetune_data.jsonl"
file_id = "file-XGinujblHPwGLSztz8cPS8XY"


def upload_file(filename):
	openai.File.create(file=open(filename), purpose='answers')

def list_files():
	openai.File.list()

def finetune(file_id):
	openai.FineTune.create(training_file=file_id)


if __name__ == '__main__':

	n = len(sys.argv)

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