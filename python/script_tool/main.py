import os
import importlib

def clear():
	print("\x1B\x5B2J", end="")
	print("\x1B\x5BH", end="")
	pass

commands = ['exit', 'cd', 'list_files', 'list_dir']
print(os.getcwd())
print(os.listdir())
input()
for file in os.listdir():
	if file.endswith('.py') and file != 'main.py':
		try:
			importlib.import_module(file[:-3])
			commands.append(file[:-3])
		except Exception as e:
			print(e)
		


while True:
	clear()
	print('Scripttool v0.1.0')
	print("Current dir : {}".format(os.getcwd()))
	print("commands : ", end='')
	print(*commands, end=' ')
	print()
	command = input().casefold()