import os

def ls(args, path):
	files = os.listdir(path)
	if len(files) == 0:
		print('No files found')
	else:
		for file in files:
			if os.path.isdir(file):
				print('\u001b[34m{}\u001b[0m'.format(file))
			else:
				print('\u001b[33m{}\u001b[0m'.format(file), end=' ')
				print('| {} bytes'.format(os.path.getsize(file)))

def list_all(args, path):
	files = os.listdir(path)
	if len(files) == 0:
		print('No files found')
	else:
		for file in files:
			if os.path.isdir(file):
				print('\u001b[34m{}\u001b[0m'.format(file))
			else:
				print('\u001b[33m{}\u001b[0m'.format(file), end=' ')
				print('| {} bytes'.format(os.path.getsize(file)))
			

def get_attr(path):
	return {
		'ls':[[], ''],
		'list_all':[[], '']
	}