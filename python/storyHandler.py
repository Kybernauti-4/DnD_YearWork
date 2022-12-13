import os
import json

def createStructure(folder):
	
	path = os.path.join(os.getcwd(),folder)
	#list_files(path)
	depth = depthFinder(path)
	#print(depth)
	with open('test.json', 'w') as json_file:
		json.dump(json.loads(createArray(path, depth)),json_file, indent=2)
			
def depthFinder(startpath):
	max_level = 0
	for root, dirs, files in os.walk(startpath):
		level = root.replace(startpath, '').count(os.sep)
		max_level = level if level > max_level else max_level

	return max_level+1

def list_files(startpath):
	for root, dirs, files in os.walk(startpath):
		level = root.replace(startpath, '').count(os.sep)
		indent = ' ' * 4 * (level)
		print('{}{}/'.format(indent, os.path.basename(root)))

		subindent = ' ' * 4 * (level + 1)
		for f in files:
			print('{}{}'.format(subindent, f))

def rindex(lst, value):
	return len(lst) - lst[::-1].index(value) - 1

def createArray(startpath, depth):
	json_array = '{'
	last_indent = -1
	max_indent = depth
	for root, dirs, files in os.walk(startpath):
		#Print part to be able to check if everything is going fine
		level = root.replace(startpath, '').count(os.sep)
		level_str = '"'+os.path.basename(root)+'"'

		#actual array part
		if level < last_indent:
			dash_index = rindex(json_array,',')
			json_array = json_array[:dash_index]
			json_array += '}'*(max_indent-level-1)+','+level_str+':{'
			last_indent = level

		elif level == last_indent:
			json_array += level_str+":["
			if len(files) != 0:
				for f in files:
					json_array += '"'+f+'"' + ','
				
				dash_index = rindex(json_array,',')
				json_array = json_array[:dash_index]

			json_array += '],'
			last_indent = level

		elif level > last_indent and level == max_indent-1:
			json_array += level_str+":["
			if len(files) != 0:
				for f in files:
					json_array += '"'+f+'"' + ','
				
				dash_index = rindex(json_array,',')
				json_array = json_array[:dash_index]

			json_array += '],'
			last_indent = level

		elif level > last_indent:
			json_array+= level_str+':{'
			last_indent = level

	dash_index = rindex(json_array,',')
	json_array = json_array[:dash_index]
	json_array += '}'*(depth)
	#print(json_array)
	return json_array
	

createStructure('story')