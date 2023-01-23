import os
import fileHandler

def clear():
	print("\x1B\x5B2J", end="")
	print("\x1B\x5BH", end="")
	pass


commands = ['exit', 'cd','cfile','edit','run']
while True:
	clear()
	print('Scripttool v0.1.0')
	curr_path = os.getcwd()
	print("Current dir : {}".format(curr_path))
	print("commands : ", end='')
	for command in commands:
		print(command, end=' ')
	print()
	check_val = input().casefold()

	if check_val in commands or check_val == '':
		pass
	else:
		print('Invalid command')
		input('Press enter to continue')
		continue

	if check_val == commands[0]:
		break
	elif check_val == commands[1]:
		print([item for item in os.listdir() if os.path.isdir(os.path.join(curr_path, item))])
		try:
			os.chdir(input('Enter directory: '))
		except:
			print('Invalid directory')
			input('Press enter to continue')
			continue
	elif check_val == commands[2]:
		print([item for item in os.listdir() if os.path.isfile(os.path.join(curr_path, item))])
		try:
			content = fileHandler.read(os.path.join(curr_path,input('Enter file: ')))
			print(content)
			input('Press enter to continue')
		except:
			print('Invalid file')
			input('Press enter to continue')
			continue