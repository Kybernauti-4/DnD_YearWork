import os

def list_dir(args, path):
	dir_list = [item for item in os.listdir(path) if os.path.isdir(item)]
	if len(dir_list) == 0:
		print('No directories found')
	else:
		print(*dir_list, sep=' ')

def ld(args, path):
	dir_list = [item for item in os.listdir(path) if os.path.isdir(item)]
	if len(dir_list) == 0:
		print('No directories found')
	else:
		print(*dir_list, sep=' ')

def get_attr(path):
	return {
		'list_dir':[[], ''],
		'ld':[[], ''],
	}