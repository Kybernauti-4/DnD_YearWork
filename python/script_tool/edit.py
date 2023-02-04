import os
import json
import keyboard

ignore_keys = ['up', 'down', 'left', 'right', 'tab', 'esc', 'enter']

def add_to_menu(e, line, horizontal, initial_cmlen, path, my_f_type, context_menu):
	#FIXME : it ain't working properly
	try:
		line[0][horizontal[0]-1]
	except IndexError:
		return

	print('add_to_menu')
	if line[0][horizontal[0]-1] == '[' and line[0][horizontal[0]] == ']':
		path_parts = path.split('\\')
		match my_f_type:
			case 'events':

				if len(context_menu) > initial_cmlen:
					return
				
				print("Ading events to context menu")
				new_path = ''
				if 'python' in path_parts:
					index = path_parts.index('python')
					index += 1
					new_path = '/'.join(path_parts[:(index)])
				else:
					print(f"python not found in {path}")
				
				with open(os.path.join(new_path, 'scriptlocation.json'), 'r') as f:
					script_location = json.load(f)
				
					for s in script_location:
						for script in [file for file in os.listdir(os.path.join(new_path, script_location[s])) if file.endswith('.py')]:
							context_menu.append(script.replace('.py', ''))

			case 'sc_info':
				
				if len(context_menu) > initial_cmlen:
					return
				
				new_path = ''
				if 'python' in path_parts:
					index = path_parts.index('python')
					index += 1
					new_path = '/'.join(path_parts[:(index)])
				else:
					print(f"python not found in {path}")
				
				with open(os.path.join(new_path, 'scriptlocation.json'), 'r') as f:
					script_location = json.load(f)
				
					for s in script_location:
						for script in [file for file in os.listdir(os.path.join(new_path, script_location[s])) if file.endswith('.py')]:
							context_menu.append(script.replace('.py', ''))
			
			case 'player':
				#TODO : add player context menu
				context_menu = ['player']

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def print_file(file_content):
	curr_line = ''
	bracket_check = False
	string_check = False
	screen = []
	for char in json.dumps(file_content, indent=4):
		if char == '[':
			bracket_check = True
		elif char == ']':
			bracket_check = False

		if char == '"':
			string_check = not string_check

		if char == '\n' and not bracket_check:
			screen.append(curr_line)
			curr_line = ''
			continue

		if bracket_check:
			if char == ' ' and not string_check:
				continue

		curr_line += char if char != '\n' else ''
	else:
		screen.append(curr_line)
	return screen

def update_variable(e, vertical, screen, line, context_menu, context, horizontal, cm_idx, indent, insert, edit_mode):
	global ignore_keys
	if not edit_mode[0]:
		if e.name == 'up':
			if vertical[0] > 0:
				curr_line = screen[vertical[0]]
				print(f'\r\u001b[0m{curr_line}', end='', flush=True)
				print(f'\r\u001b[A', end='', flush=True)

				vertical[0] -= 1
				curr_line = screen[vertical[0]]
				print(f'\u001b[32m{curr_line}\u001b[0m', end = '', flush=True)


		if e.name == 'down':
			if vertical[0] < len(screen) - 1:
				curr_line = screen[vertical[0]]
				print(f'\r\u001b[0m{curr_line}', end='', flush=True)
				print(f'\r\u001b[B', end='', flush=True)

				vertical[0] += 1
				curr_line = screen[vertical[0]]
				print(f'\u001b[32m{curr_line}\u001b[0m', end = '', flush=True)
		
		
		if e.name == 'enter':
			curr_line = screen[vertical[0]]
			print(f'\r\u001b[33m{curr_line}\u001b[0m', end='', flush=True)
			down_num = len(screen) - vertical[0] 
			print(f'\r\u001b[{down_num}B{curr_line.strip()}', end='', flush=True)
			for char in curr_line:
				if char != ' ':
					break
				else:
					indent[0] += 1
			line[0] = curr_line.strip()
			horizontal[0] = len(line[0])
			edit_mode[0] = True

		if e.name == 'n':
			#FICXME : ASYNC destroys this logic
			insert[0] = True
			line[0] = 'new_line'
			flush_input()
			down_num = len(screen) - vertical[0] 
			print(f'\r\u001b[{down_num}B', end='', flush=True)
			print('Please enter the indent level: ', end='', flush=True)
			indent[0] = int(input())
			print(f'\r\u001b[0m', end='', flush=True)
			horizontal[0] = len(line[0])
			print(f'{line[0]}', end='', flush=True)
			flush_input()
			edit_mode[0] = True
		
		if e.name == 'r':
			#! SAFEFAULT : this is a safe fault, if the file is not a json file, it will crash
			print(f'\r\u001b[{len(screen)-1}A\u001b[J', end='', flush=True)
			new_screen = print_file(json.loads(''.join(screen)))
			screen.clear()
			for line in new_screen:
				screen.append(line)
			for i in range(len(screen)):
				if i != len(screen) - 1:
					print(screen[i])
				else:
					print(screen[i], end = '', flush=True)
			vertical[0] = len(screen) - 1
			




	else:
		if e.name == 'up':
			if len(context[0]) > 0:
				del_len = len(context[0]) + len(line[0][horizontal[0]:])
				print(f'\u001b[{del_len}D\u001b[K', end='', flush=True)
				print(f'\u001b[34m{context_menu[cm_idx[0]]}\u001b[0m', end='', flush=True)
				print(f'{line[0][horizontal[0]:]}', end='', flush=True)
				context[0] = context_menu[cm_idx[0]]
				cm_idx[0] += 1
				if cm_idx[0] >= len(context_menu):
					cm_idx[0] = 0
				
			else:
				print(f'\u001b[34m{context_menu[cm_idx[0]]}\u001b[0m\u001b[K', end='', flush=True)
				print(f'{line[0][horizontal[0]:]}', end='', flush=True)
				context[0] = context_menu[cm_idx[0]]
				cm_idx[0] += 1
				if cm_idx[0] >= len(context_menu):
					cm_idx[0] = 0

		elif e.name == 'left' and len(context[0]) == 0:
			print(f'\u001b[D', end='', flush=True)
			horizontal[0] -= 1

		elif e.name == 'right' and len(context[0]) == 0:
			print(f'\u001b[C', end='', flush=True)
			horizontal[0] += 1

		elif e.name == 'down' and len(context[0]) > 0:
			print(f'\r\u001b[K{line[0]}', end='', flush=True)
			print(f'\u001b[{len(line[0]) - horizontal[0]}D', end='', flush=True)
			cm_idx[0] = 0
			context[0] = ''

		elif e.name == 'tab':
			line[0] = line[0][:horizontal[0]] + context[0] + line[0][horizontal[0]:]
			print(f'\r\u001b[K{line[0]}', end='', flush=True)
			print(f'\u001b[{len(line[0]) - horizontal[0] -1}D', end='', flush=True)
			horizontal[0] += 1
			cm_idx[0] = 0
			context[0] = ''
		
		elif e.name == 'backspace':
			if len(context[0]) != 0:
				print(f'\r\u001b[K{line[0]}', end='', flush=True)
				print(f'\u001b[{len(line[0]) - horizontal[0]}D', end='', flush=True)
				cm_idx[0] = 0
				context[0] = ''
			else:
				line[0] = line[0][:horizontal[0]-1] + line[0][horizontal[0]:]
				horizontal[0] -= 1
				print(f'\r\u001b[K{line[0]}', end='', flush=True)
				print(f'\r\u001b[{horizontal[0]}C', end='', flush=True)
		
		elif e.name == 'delete' and len(context[0]) == 0:
			line[0] = line[0][:horizontal[0]] + line[0][horizontal[0]+1:]
			print(f'\r\u001b[K{line[0]}', end='', flush=True)
			print(f'\r\u001b[{horizontal[0]}C', end='', flush=True)

		elif e.name == 'enter':
			if line[0] == '':
				if insert[0]:
					pass
				else:
					del screen[vertical[0]]
			else:
				if insert[0]:
					add_line = ' '*indent[0] + line[0]
					screen.insert(vertical[0], add_line)
				else:
					screen[vertical[0]] = ' '*indent[0] + line[0]

			line[0] = ''
			context[0] = ''
			cm_idx[0] = 0
			indent[0] = 0
			print(f'\r\u001b[{len(screen)}A\033[J', end='', flush=True)

			for i in range(len(screen)):
				if i != len(screen) - 1:
					print(screen[i])
				else:
					print(screen[i], end = '', flush=True)
					
			vertical[0] = len(screen) - 1
			edit_mode[0] = False


		elif e.event_type == keyboard.KEY_DOWN and e.name not in keyboard.all_modifiers and e.name not in ignore_keys:
			line[0] = line[0][:horizontal[0]] + (e.name if e.name != 'space' else ' ') + line[0][horizontal[0]:]
			horizontal[0] += 1
			print(f'\r\u001b[K{line[0]}', end='', flush=True)
			print(f'\r\u001b[{horizontal[0]}C', end='', flush=True)

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
		vertical = [0]

		screen = print_file(file_content)

		for i in range(len(screen)):
			if i != len(screen) - 1:
				print(screen[i])
			else:
				print(screen[i], end = '', flush=True)

		vertical[0] = len(screen) - 1
		horizontal = [len(screen[-1])]

		line = ['']
		context_menu = ["[]", "{}", "\"\"", ":", "()"]
		initial_cmlen = len(context_menu)
		context = ['']
		cm_idx = [0]
		indent = [0]
		insert = [False]
		edit_mode = [False]

		keyboard.on_press(lambda e: update_variable(e, vertical, screen, line, context_menu,context, horizontal, cm_idx, indent, insert, edit_mode))
		keyboard.on_release(lambda e: add_to_menu(e, line, horizontal, initial_cmlen, path, my_f_type, context_menu))	

		keyboard.wait('esc')
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

def e(args, path):
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
		vertical = [0]

		screen = print_file(file_content)

		for i in range(len(screen)):
			if i != len(screen) - 1:
				print(screen[i])
			else:
				print(screen[i], end = '', flush=True)

		vertical[0] = len(screen) - 1
		horizontal = [len(screen[-1])]

		line = ['']
		context_menu = ["[]", "{}", "\"\"", ":", "()"]
		initial_cmlen = len(context_menu)
		context = ['']
		cm_idx = [0]
		indent = [0]
		insert = [False]

		keyboard.on_press(lambda e: update_variable(e, vertical, screen, line, context_menu,context, horizontal, cm_idx, indent))
		keyboard.on_press(lambda e: add_to_menu(e, line, horizontal, initial_cmlen, path, my_f_type, context_menu))	

		keyboard.wait('esc')
		keyboard.unhook_all()
		flush_input()
	
def get_attr(path):

	return_dict = {
		'create': [['json', 'txt', 'sc_info', 'events', 'player'],''],
		'c':[['json', 'txt', 'sc_info', 'events', 'player'],''],
		'edit': [['__local_files__'],'No files found'],
		'e': [['__local_files__'],'No files found'],
	}

	return return_dict


if __name__ == '__main__':
	edit(['Test.json','events'], os.path.dirname(__file__))