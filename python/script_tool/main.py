import importlib
import os
import sys

import keyboard

#TODO: Add command line tags
#TODO: Add importable commands

runtime_path = os.path.dirname(__file__)
os.chdir(runtime_path)

#----------------- context menu -----------------#
base_commands = {
	'cd':[[item for item in os.listdir() if os.path.isdir(item)], 'No directory found']
}
r_commands = {}
r_commands.update(base_commands)
ignore_keys = ['up', 'down', 'left', 'right', 'tab', 'esc', 'enter']

def update_cmenu(command, new_cmenu='', new_invalid_message=''):
	global r_commands
	global base_commands
	if command in r_commands.keys():
		r_commands[command][0] = new_cmenu if new_cmenu != '' else r_commands[command][0]
		r_commands[command][1] = new_invalid_message if new_invalid_message != '' else r_commands[command][1]
	

#!----------------- update_variable == screen -----------------#
def update_variable(e, my_variable, context):
	global ignore_keys
	#'cd':[[context menu][invalid message]]
	global r_commands


	curr_command = ''.join(my_variable).strip().casefold()
	if curr_command in r_commands.keys():
		context_menu = r_commands[curr_command][0]
		invalid_message = r_commands[curr_command][1]
		if e.name in ['up', 'down'] and len(context) == 0:
			if len(context_menu) == 0:
				print("\033[96m{}\033[00m".format(invalid_message), end=' ', flush=True)
				context.append(invalid_message)
				context.append(' ')
			for context_item in context_menu:
				print("\033[96m{}\033[00m".format(context_item), end=' ', flush=True)
				context.append(context_item)
				context.append(' ')

	if e.name in ['left', 'right'] and len(context) > 2:
		del_len = 0
		nows_context = [elem for elem in context if elem != ' ']
		for i in range(len(context)):
			del_len += len(context.pop())
		for i in range(del_len):
			print('\b\033[K', end='', flush=True)

		if e.name == 'left':
			nows_context.append(nows_context.pop(0))
			for elem in nows_context:
				context.append(elem)
				context.append(' ')
				print("\033[96m{}\033[00m".format(elem), end=' ', flush=True)

		elif e.name == 'right':
			nows_context.insert(0, nows_context.pop())
			for elem in nows_context:
				context.append(elem)
				context.append(' ')
				print("\033[96m{}\033[00m".format(elem), end=' ', flush=True)

	if e.name == 'tab' and len(context) > 0:
		del_len = 0
		#? no_whitespace_context
		nows_context = [elem for elem in context if elem != ' ']
		choice = nows_context[0]
		for elem in context:
			del_len += len(elem)
		for i in range(del_len):
			print('\b\033[K', end='', flush=True)

		if choice != invalid_message:
			print(choice, end='', flush=True)
			if my_variable[-1] != ' ': my_variable.append(' ')
			my_variable.append(choice)
		context.clear()
		
	if e.name == "space":
		my_variable.append(" ")
		print(' ', end='', flush=True)

	elif e.name == "backspace":
		try:
			if len(context) > 0:
				del_len = 0
				for celem in context:
					del_len += len(celem)
				for i in range(del_len):
					print('\b\033[K', end='', flush=True)
				context.clear()
			else:
				del_len = len(my_variable.pop())
				for i in range(del_len):
					print('\b\033[K', end='', flush=True)
		except Exception as e:
			print(e)
			pass

	elif e.event_type == keyboard.KEY_DOWN and e.name not in keyboard.all_modifiers and e.name not in ignore_keys:
		my_variable.append(e.name)
		print(e.name, end='', flush=True)

def get_input():
	context = []
	command = []
	keyboard.on_press(lambda e: update_variable(e,command, context))
	keyboard.wait('enter')
	keyboard.unhook_all()
	input()
	print('\r\033[K', end='', flush=True)
	return ''.join(command)

def clear():
	print("\x1B\x5B2J", end="")
	print("\x1B\x5BH", end="")
	pass

#-------------------------	main -------------------------#

# commands {'command_file': {'command': [context menu, invalid message]}}

import_commands = {}

for file in [f for f in os.listdir() if os.path.isfile(f)]:
	if  file == 'main.py':
		continue
	elif file == 'fileHandler.py':
		continue
	else:
		#print('Importing {}'.format(file))
		#input()
		try:
			#TODO: Complete this

			importlib.import_module(file.replace('.py', ''))
			extra_data = getattr(sys.modules[file.replace('.py', '')], 'get_attr')(os.getcwd())
			command_data = {file.replace('.py', ''): extra_data}
			import_commands.update(command_data)
		except Exception as e:
			print(e)


for file,data in import_commands.items():
	r_commands.update(data)

command_keys = list(r_commands.keys())

while __name__ == '__main__':
	clear()
	print('Scripttool v0.1.0')
	print("Current dir : {}".format(os.getcwd()))
	print("commands : ", end='')
	print(*command_keys, end=' ')
	print()
	command_list = get_input().split(' ')
	command = command_list[0].casefold()
	args = command_list[1:]
	if len(args) == 0:
		args.append('')
	for arg in args:
		if arg == '' and args.index(arg) != 1:
			args.remove(arg)

	if command == 'exit':
		break
	elif command == 'cd':
		for arg in args:
			os.chdir(arg)
		if arg == '':
			os.chdir('..')
		new_menu = [item for item in os.listdir() if os.path.isdir(item)]
		update_cmenu('cd', new_cmenu = new_menu)
	elif command in command_keys:
		command_file = ''
		for file, data in import_commands.items():
			if command in list(data.keys()):
				command_file = file
				break
		try:
			updated_cmenu, updated_msg = getattr(sys.modules[command_file], command)(args, os.getcwd())
			if updated_cmenu != None:
				update_cmenu(command, new_cmenu = updated_cmenu)
			if updated_msg != None:
				updated_cmenu(command, new_invalid_message = updated_msg)
			input('Press enter to return to main menu')
		except:
			print('Error in {}'.format(command))
			input('Press enter to return to main menu')