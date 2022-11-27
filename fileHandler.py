import json

def read(filename):
	try:
		file = open(filename, 'r')
	except:
		print("file doesn't exist")
		return {'input':'None'}
	
	if '.json' in filename:
		file_dict : dict = json.load(file)
		return file_dict
	else:
		return file

def write(filename, strToWrite):
	with open(filename, 'w') as file:
		if '.json' in filename:
			json.dump(strToWrite,file)
		else:
			file.write(strToWrite)


def append(filename, strToAppend):
	with open(filename, 'a') as file:
		file.write(strToAppend)

def rewriteJSON(filename, field, strToReplace, newStr):
	if '.json' in filename:
		edit_str = read(filename)
		edit_str[field] = edit_str[field].replace(strToReplace, newStr)
		write(filename, edit_str)
		return 'done'
	else:
		raise Exception('Wrong file type')
