import os
import fileHandler
import json




main_commands = ['exit', 'cd', 'cf']
cf_commands = ['exit', 'cd', 'cf', 'write', 'clear']
file_content = ''
check_val = ''
while True:
	if check_val == '':
		pass
	else:
		input('Press enter to continue')
	clear()
	print('Scripttool v0.1.0')
	curr_path = os.getcwd()
	print("Current dir : {}".format(curr_path))
	print("commands : ", end='')
	print(*main_commands, end=' ')
	print()
	
	check_val = input().casefold()

	if check_val in main_commands or check_val == '':
		pass
	else:
		print('Invalid command')
		continue
	# ---------------------------- command 1 ----------------------------
	if check_val == main_commands[0]:
		break
	# ---------------------------- command 2 ----------------------------
	elif check_val == main_commands[1]:
		dirs =[item for item in os.listdir() if os.path.isdir(os.path.join(curr_path, item))]
		if len(dirs) > 0:
			print(dirs)
		else:
			print('No directories')
			continue
		try:
			os.chdir(input('Enter directory: '))
		except:
			print('Invalid directory')
			continue
	# ---------------------------- command 3 ----------------------------
	elif check_val == main_commands[2]:
		files = [item for item in os.listdir() if os.path.isfile(os.path.join(curr_path, item))]
		if len(files) > 0:
			print(files)
		else:
			print('No files')
			continue
		try:
			file_content = fileHandler.read(os.path.join(curr_path, curr_file :=input('Enter file: ')))
			if curr_file.endswith('.json'):
				print(json.dumps(file_content, indent=2))
			else:
				print(file_content)
		except:
			print('Invalid file')
			continue
