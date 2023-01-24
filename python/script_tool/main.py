import importlib
import os
import sys

import keyboard

#TODO: Add command line tags
#TODO: Add importable commands

#----------------- context menu -----------------#

def update_variable(e, my_variable, context, extra_data):
	ignore_keys = ['up', 'down', 'left', 'right', 'tab', 'esc']
	
	#'cd':[[context menu][invalid message]]
	
	base_commadns = {
		'cd':[[item for item in os.listdir() if os.path.isdir(item)], 'No directory found'],
	}
	if len(extra_data) > 0:
		base_commadns.update(extra_data)


	curr_command = ''.join(my_variable).strip().casefold()
	if curr_command in base_commadns.keys():
		context_menu = base_commadns[curr_command][0]
		invalid_message = base_commadns[curr_command][1]
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
				del_len = len(context.pop())
				for i in range(del_len):
					print('\b\033[K', end='', flush=True)
			else:
				del_len = len(my_variable.pop())
				for i in range(del_len):
					print('\b\033[K', end='', flush=True)
		except:
			pass
	elif e.name == "enter":
		pass
	elif e.event_type == keyboard.KEY_DOWN and e.name not in keyboard.all_modifiers and e.name not in ignore_keys:
		my_variable.append(e.name)
		print(e.name, end='', flush=True)

def get_input(extra_data={}):
	context = []
	command = []
	keyboard.on_press(lambda e: update_variable(e,command, context, extra_data))
	keyboard.wait('enter')
	keyboard.unhook_all()
	input()
	print('\r\033[K', end='', flush=True)
	return ''.join(command)

runtime_path = os.path.dirname(__file__)
os.chdir(runtime_path)

def clear():
	print("\x1B\x5B2J", end="")
	print("\x1B\x5BH", end="")
	pass

#-------------------------	main -------------------------#

# commands {'command_file': {'command': [context menu, invalid message]}}

commands = {}

for file in [f for f in os.listdir() if os.path.isfile(f)]:
	if  file == 'main.py':
		continue
	elif file == 'fileHandler.py':
		continue
	else:
		#print('Importing {}'.format(file))
		input()
		try:
			importlib.import_module(file.replace('.py', ''))
			extra_data = getattr(sys.modules[file.replace('.py', '')], 'get_attr')(os.getcwd())
			commands.append(file.replace('.py', ''))
		except Exception as e:
			print(e)
		
while __name__ == '__main__':
	clear()
	print('Scripttool v0.1.0')
	print("Current dir : {}".format(os.getcwd()))
	print("commands : ", end='')
	print(*commands, end=' ')
	print()
	command_list = get_input().split(' ')
	command = command_list[0]
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
	elif command in commands:
		try:
			getattr(sys.modules[command], 'main')(args, os.getcwd())
		except:
			print('Error in {}'.format(command))
			input('Press enter to continue')