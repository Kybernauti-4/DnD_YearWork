import json
import os


def read(filename):
	try:
		file = open(filename, 'r')
	except:
		#print("file doesn't exist")
		return {'input':'None'}
	
	if '.json' in filename:
		file_dict : dict = json.load(file)
		file.close()
		return file_dict
	else:
		data = file.read()
		file.close()
		return data

def _readRaw(filename):
	try:
		file = open(filename, 'r')
		data = file.read()
		file.close()
		return data
	except:
		#print("file doesn't exist")
		return None

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

def _writeRaw(filename, data):
	with open(filename, 'w') as file:
		file.write(data)


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

def loadSave(path):
	src = os.path.join(path,'.orig')
	if not os.path.exists(src):
		return False
	if __name__ == '__main__':
		print("It's happening, let us pray brothers and sisters")
	for root, dirs, files in os.walk(path):
		for filename in files:
			exclude = False
			for i in os.path.dirname(os.path.join(root, filename)).split(os.path.sep):
				if i.startswith('.'):
					exclude = True
					break
			if exclude:continue
			os.remove(os.path.join(root, filename))
		
	for root,dirs,files in os.walk(src):
		for filename in files:
			dst = root.replace('\\.orig','')
			_writeRaw(os.path.join(dst,filename),_readRaw(os.path.join(root,filename)))


if __name__ == "__main__":
	loadSave('story\\Chapter_1\\Encounter_1\\Scene_1')
	print('Done')
