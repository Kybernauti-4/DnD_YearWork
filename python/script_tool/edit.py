def edit(path):
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
	
def get_attr(path):
	create_command = ['create', 'c']
	create_options = ['json', 'txt', 'sc_info', 'events', 'player', 'player_template']
	tags = ['-empty', '-e', '-notepad', '-np']
	for command in create_command:
		return_dict.update({command: [create_options, '']})

	return_dict = {}
	return return_dict