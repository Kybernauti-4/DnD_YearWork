import importlib
import os
from sys import stdin

import keyboard


def update_variable(e, my_variable, context):
	folders = [item for item in os.listdir() if os.path.isdir(item)]
	if (''.join(my_variable)).strip() == 'cd':
		if e.name in ['up', 'down'] and len(context) == 0:
			for folder in folders:
				print("\033[96m{}\033[00m".format(folder), end=' ', flush=True)
				context.append(folder)
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
		for elem in context:
			del_len += len(elem)
		for i in range(del_len):
			print('\b\033[K', end='', flush=True)
		
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
	elif e.event_type == keyboard.KEY_DOWN and e.name not in keyboard.all_modifiers and e.name not in ['up', 'down', 'left', 'right']:
		my_variable.append(e.name)
		print(e.name, end='', flush=True)

def get_input():
	context = []
	command = []
	keyboard.on_press(lambda e: update_variable(e,command, context))
	keyboard.wait('enter', suppress=True)
	keyboard.unhook_all()
	return ''.join(command)

runtime_path = os.path.dirname(__file__)
os.chdir(runtime_path)

def clear():
	print("\x1B\x5B2J", end="")
	print("\x1B\x5BH", end="")
	pass

commands = ['exit', 'cd', 'list_files', 'list_dir']

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
	command = get_input()
	print()
	print('Command entered : {}'.format(command))
	input('Press enter to continue...')