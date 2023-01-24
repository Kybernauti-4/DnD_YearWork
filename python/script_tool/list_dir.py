import os

def list_dir(args, path):
	dir_list = [item for item in os.listdir(path) if os.path.isdir(item)]
	if len(dir_list) == 0:
		print('No directories found')
	else:
		for dir in dir_list:
			print('\u001b[34m{}\u001b[0m'.format(dir))

def ld(args, path):
	dir_list = [item for item in os.listdir(path) if os.path.isdir(item)]
	if len(dir_list) == 0:
		print('No directories found')
	else:
		for dir in dir_list:
			print('\u001b[34m{}\u001b[0m'.format(dir))

def get_attr(path):
	return {
		'list_dir':[[], ''],
		'ld':[[], ''],
	}