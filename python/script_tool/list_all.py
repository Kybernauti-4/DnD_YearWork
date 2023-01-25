import os

def ls(args, path):
	files = os.listdir(path)
	if len(files) == 0:
		print('\033[31m{}\033[0m'.format('Nothing found'))
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
		print('\033[31m{}\033[0m'.format('Nothing found'))
	else:
		for file in files:
			if os.path.isdir(file):
				print('\u001b[34m{}\u001b[0m'.format(file))
			else:
				print('\u001b[33m{}\u001b[0m'.format(file), end=' ')
				print('| {} bytes'.format(os.path.getsize(file)))

def lf(args, path):
	files = [file for file in os.listdir(path) if os.path.isfile(file)]
	if len(files) == 0:
		print('\033[31m{}\033[0m'.format('No files found'))
	else:
		for file in files:
			print('\u001b[33m{}\u001b[0m'.format(file), end=' ')
			print('| {} bytes'.format(os.path.getsize(file)))

def list_files(args, path):
	files = [file for file in os.listdir(path) if os.path.isfile(file)]
	if len(files) == 0:
		print('\033[31m{}\033[0m'.format('No files found'))
	else:
		for file in files:
			print('\u001b[33m{}\u001b[0m'.format(file), end=' ')
			print('| {} bytes'.format(os.path.getsize(file)))

def list_dir(args, path):
	dir_list = [item for item in os.listdir(path) if os.path.isdir(item)]
	if len(dir_list) == 0:
		print('\033[31m{}\033[0m'.format('No directiories found'))
	else:
		for dir in dir_list:
			print('\u001b[34m{}\u001b[0m'.format(dir))

def ld(args, path):
	dir_list = [item for item in os.listdir(path) if os.path.isdir(item)]
	if len(dir_list) == 0:
		print('\033[31m{}\033[0m'.format('No directiories found'))
	else:
		for dir in dir_list:
			print('\u001b[34m{}\u001b[0m'.format(dir))
			

def get_attr(path):
	return {
		'ls':[[], ''],
		'list_all':[[], ''],
		'lf':[[], ''],
		'list_files':[[], ''],
		'list_dir':[[], ''],
		'ld':[[], '']
	}