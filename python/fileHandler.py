import json
import os


def read(filename):
	try:
		file = open(filename, 'r')
	except:
		print("file doesn't exist")
		return {'input':'None'}
	
	if '.json' in filename:
		file_dict : dict = json.load(file)
		file.close()
		return file_dict
	else:
		data = file.read()
		file.close()
		return data

def readJSON(filename,field):
	if '.json' in filename:
		try:
			file = open(filename, 'r')
		except Exception as e:
			print(e)
			return 'NoFileError'
		data = json.load(file)
		file.close()
		return data[field]

def write(filename, strToWrite):
	with open(filename, 'w') as file:
		if '.json' in filename:
			json.dump(str(strToWrite),file)
		else:
			file.write(str(strToWrite))


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

def getFolder(path, folder):
	return os.path.join(path, folder)
