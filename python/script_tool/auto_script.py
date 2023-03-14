import json
import os

def auto(args, path):

	path_parts = path.split('\\')
	print(path_parts)
	story_index = 0
	for index,part in enumerate(path_parts):
		if part == 'story':
			story_index = index
			break

	#print('\\'.join(path_parts[:story_index]))
	os.chdir('\\'.join(path_parts[:story_index]))

	files = [file.replace('.py','') for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and file != 'info.json']
	#print(files)
	#print(os.getcwd())
	with open('scriptlocation.json', 'r') as f:
		scripts_locations = json.load(f)

	max_id = 0
	for index,location in scripts_locations.items():
		if location == path.split('\\')[-1]:
			continue
		with open(os.path.join(location, 'info.json'), 'r') as f:
			temp_info = json.load(f)
			for sid in list(temp_info['id'].values()):
				if sid > max_id:
					max_id = sid

	with open(os.path.join(path,'info.json'), 'r') as f:
		info = json.load(f)

	grade = 10
	if len(info['id']) == 0:
		i = 0
		while max_id/pow(grade,i)>1:
			i+=1
		grade = i

	if len(info['id']) != len(files):
		for file_outside in files:
			for file_inside,id in info['id'].items():
				if file_outside == file_inside:
					break
			else:
				include = input('Do you want to include ' + file_outside + '? (y/n) :')
				if include == 'y':
					try:
						id+1
					except:
						id = pow(10,grade)

					info['id'][file_outside] = id+1
				
					for setting,field in info['info'].items():
						include = input('Do you want to the function in ' + setting + '? (y/n) :')
						if include == 'y':
							field.append(id+1)
	print('Saving...')
	with open(os.path.join(path, 'info.json'), 'w') as f:
		json.dump(info, f, indent=4)
	print('Done!')

def get_attr(path):
	return_dict = {
		'auto':[[''],'']
	}
	
	return return_dict

if __name__ == '__main__':
	auto(['',''],'story/player_scripts')