import os

def main(args, path):
	print(args)

def get_attr(path):
	return {
		'list_dir':[[file for file in os.listdir() if os.path.isdir(file)], 'No directories in directory']
	}