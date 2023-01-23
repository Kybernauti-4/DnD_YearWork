import os
import importlib
import keyboard

def update_variable(e, my_variable):
	if e.name == "space":
		my_variable.append(" ")
		print(' ', end='', flush=True)
	elif e.name == "backspace":
		try:
			my_variable.pop()
			print('\b\033[K', end='', flush=True)
		except:
			pass
	elif e.name == "enter":
		pass
	elif e.event_type == keyboard.KEY_DOWN and e.name not in keyboard.all_modifiers:
		my_variable.append(e.name)
		print(e.name, end='', flush=True)

def get_input():
	command = []
	keyboard.on_press(lambda e: update_variable(e,command))
	keyboard.wait('enter')
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