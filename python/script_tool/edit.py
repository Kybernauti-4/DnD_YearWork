def edit(args, path):
	print('What am I supposed to edit?')

def create(args, path):
	file_type = args[0]
	match file_type:
		case 'json':
			print('Creating a json file')
		case 'txt':
			print('Creating a txt file')
		case 'sc_info':
			print('Creating a sc_info file')
		case 'events':
			print('Creating an events file')
		case 'player':
			print('Creating a player file')
		case 'player_template':
			print('Creating a player_template file')
		case _:
			print('Invalid file type')

def c(args, path):
	file_type = args[0]
	match file_type:
		case 'json':
			print('Creating a json file')
		case 'txt':
			print('Creating a txt file')
		case 'sc_info':
			print('Creating a sc_info file')
		case 'events':
			print('Creating an events file')
		case 'player':
			print('Creating a player file')
		case 'player_template':
			print('Creating a player_template file')
		case _:
			print('Invalid file type')
	
def get_attr(path):

	return_dict = {
		'create': [['json', 'txt', 'sc_info', 'events', 'player', 'player_template'],''],
		'c':[['json', 'txt', 'sc_info', 'events', 'player', 'player_template'],''],
		'edit': [['path_files'],'No files found'],
		'e': [['path_files'],'No files found'],
		}
	return return_dict