import os

def main(args, path):
	print(args)

def get_attr(path):
	return {
		'list_files':[[file for file in os.listdir() if os.path.isfile(file)], 'No files in directory']
	}