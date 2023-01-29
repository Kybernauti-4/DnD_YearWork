import os
import json
import keyboard

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def update_variable(e,line, context, context_menu, vertical, horizontal, screen):

	if e.name == 'up' and len(context) == 0:
		print(f'\u001b[A', end='', flush=True)
		vertical[0] -= 1
		try:
			line = screen[vertical[0]]
			print(f'\u001b[32m{line}\u001b[0m', end = '', flush=True)
		except IndexError:
			vertical[0] += 1

	if e.name == 'down' and len(context) == 0:
		vertical[0] += 1
		try:
			line = screen[vertical[0]]
			print(f'\u001b[B', end='', flush=True)
			print(f'\u001b[32m{line}\u001b[0m', end = '', flush=True)
		except IndexError:
			vertical[0] -= 1


	if e.name == 'left':
		print(f'\u001b[D', end='', flush=True)
	if e.name == 'right':
		print(f'\u001b[C', end='', flush=True)

def edit(args, path):
	file_types = {}
	with open(os.path.join(os.path.dirname(__file__), 'file_types.json'), 'r') as f:
		file_types = json.load(f)
	
	try:
		file = args[0]
	except IndexError:
		print('Invalid file')
		return

	try:
		my_f_type = args[1]
	except IndexError:
		while True:
			for f in file_types:
				print(f, end=' ')
			print()
			print('Provide a file type : ', end='')
			my_f_type = input().casefold().strip()

			if my_f_type not in file_types:
				print('Unsupported file type')
			else:
				break

	file_type = file_types[my_f_type]

	if file_type == 'txt':
		os.system('notepad.exe ' + file)

	elif file_type == 'json':
		with open(os.path.join(path,file), 'r') as f:

			file_content = json.load(f)
			curr_line = ''

			screen = []
			for char in json.dumps(file_content, indent=4):
				if char == '\n':
					screen.append(curr_line)
					curr_line = ''
					continue
				curr_line += char
			else:
				screen.append(curr_line)

			for line in screen:
				print(line)

			context_menu = ['[]', '\{\}', '""', ":", '()']
			initial_cmlen = len(context_menu)
			
			context = []
			vertical = [len(screen)+1]
			horizontal = [0]
			line = []

			keyboard.on_press(lambda e: update_variable(e,line, context, context_menu, vertical, horizontal, screen))

			while True:
				index = horizontal[0]

				try:
					line[index-1]
				except IndexError:
					continue
				
				if line[index-1] == '[' and line[index+1] == ']':
					path_parts = path.split('/')
					match my_f_type:
						case 'events':

							if len(context_menu) > initial_cmlen:
								continue

							if 'python' in path_parts:
								index = path_parts.index('python')
								new_path = '/'.join(path_parts[:index+1])
							else:
								print(f"python not found in {path}")
							
							with open(os.path.join(new_path, 'scriptlocation.json'), 'r') as f:
								script_location = json.load(f)
							
							for s in script_location:
								for script in [file for file in os.listdir(os.path.join(new_path, s)) if file.endswith('.py')]:
									context_menu.append(script.replace('.py', ''))

						case 'sc_info':
							context_menu = ['sc_info']
						
						case 'player':
							context_menu = ['player']

				else:
					context_menu = ['[]', '\{\}', '""', ":", '()']
							

				if ''.join(line) == 'exit': 
					print('exit')
					break
			keyboard.unhook_all()
			flush_input()



def create(args, path):
	try:
		file_type = args[0].casefold().strip()
	except IndexError:
		file_type = args.casefold().strip()

	try:
		with open(os.path.join(os.path.dirname(__file__),'file_types.json'), 'r') as f:
			file_types = json.load(f)
	except FileNotFoundError:
		print('File types not found')
		return

	print('Provide a file name : ', end='')
	file_name = input()
	try:
		open(os.path.join(path, (file_name + '.' +file_types[file_type])), 'x')
		print('File created')
	except FileExistsError:
		print('File already exists')
		return
	
	
	print('Do you want to edit the file? (y/n) : ', end='')
	edit = input().casefold().strip()

	if edit == 'y':
		edit([f, file_type], path)


def c(args, path):
	try:
		file_type = args[0].casefold().strip()
	except IndexError:
		file_type = args.casefold().strip()

	try:
		with open(os.path.join(os.path.dirname(__file__),'file_types.json'), 'r') as f:
			file_types = json.load(f)
	except FileNotFoundError:
		print('File types not found')
		return

	print('Provide a file name : ', end='')
	file_name = input()
	try:
		open(os.path.join(path, (file_name + '.' +file_types[file_type])), 'x')
		print('File created')
	except FileExistsError:
		print('File already exists')
		return
	
	
	print('Do you want to edit the file? (y/n) : ', end='')
	edit = input().casefold().strip()

	if edit == 'y':
		edit([f, file_type], path)
	
def get_attr(path):

	return_dict = {
		'create': [['json', 'txt', 'sc_info', 'events', 'player'],''],
		'c':[['json', 'txt', 'sc_info', 'events', 'player'],''],
		'edit': [['__local_files__'],'No files found'],
		'e': [['__local_files__'],'No files found'],
	}

	return return_dict


if __name__ == '__main__':
	edit(['Test.json'], os.path.dirname(__file__))