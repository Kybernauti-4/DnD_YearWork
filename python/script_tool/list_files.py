import os

def lf(args, path):
	files = [file for file in os.listdir(path) if os.path.isfile(file)]
	if len(files) == 0:
		print('No files found')
	else:
		for file in files:
			print('\u001b[33m{}\u001b[0m'.format(file), end=' ')
			print('| {} bytes'.format(os.path.getsize(file)))

def list_files(args, path):
	files = [file for file in os.listdir(path) if os.path.isfile(file)]
	if len(files) == 0:
		print('No files found')
	else:
		for file in files:
			print('\u001b[33m{}\u001b[0m'.format(file), end=' ')
			print('| {} bytes'.format(os.path.getsize(file)))

def get_attr(path):
	return {
		'lf':[[], ''],
		'list_files':[[], '']
	}