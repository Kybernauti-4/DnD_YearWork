import os

def ls(args, path):
	files = [file for file in os.listdir(path) if os.path.isfile(file)]
	if len(files) == 0:
		print('No files found')
	else:
		print(*files, sep=' ')

def list_files(args, path):
	files = [file for file in os.listdir(path) if os.path.isfile(file)]
	if len(files) == 0:
		print('No files found')
	else:
		print(*files, sep=' ')

def get_attr(path):
	return {
		'ls':[[], ''],
		'list_files':[[], '']
	}