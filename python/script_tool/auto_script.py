import json
import os


def auto(args, path):
	os.chdir(path)
	files = [file.replace('.py','') for file in os.listdir() if os.path.isfile(file) and file != 'info.json']
	print(files)
	with open('info.json', 'r') as f:
		info = json.load(f)

	if len(info['id']) != len(files):
		for file_outside in files:
			for file_inside,id in info['id'].items():
				if file_outside == file_inside:
					break
			else:
				include = input('Do you want to include ' + file_outside + '? (y/n) :')
				if include == 'y':
					info['id'][file_outside] = id+1
				
					for setting,field in info['info'].items():
						include = input('Do you want to the function in ' + setting + '? (y/n) :')
						if include == 'y':
							field.append(id+1)
	
	with open('info.json', 'w') as f:
		json.dump(info, f, indent=4)

def get_atrr(path):
	return_dict = {
		'auto':['','']
	}
	
	return return_dict

if __name__ == '__main__':
	auto(['',''],'story/player_scripts')