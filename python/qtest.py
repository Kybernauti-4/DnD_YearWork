import os
import sys
import keyboard

cli_cmd_list = [    ['set prompt','f_set_prompt'], 
					['show files','f_show_files'],
					['show dirs','f_show_dirs'],
					['show date','f_show_date']
				]

def print_message(msg):
	print(f'{msg}')

def update_variable(e, my_variable):
	if e.name == "space":
		my_variable.append(" ")
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

def isValidCmd(entered_cmd):   
	for c in cli_cmd_list:
		e_cmd = "".join(entered_cmd.split())
		v_cmd = "".join(str(c[0]).split())
		if e_cmd == v_cmd:
			return True, str(c[1])
	return False, entered_cmd

def str_to_class(classname):
	return getattr(sys.modules[__name__], classname)

def f_set_prompt():
	global prompt
	print_message('Prompting for new prompt.')
	prompt = input('Enter new prompt : ')

def f_show_dirs():
	print_message('Showing only directories')
	os.system('dir /ad')

def f_show_files():
	print_message('Showing only files')
	os.system('dir /b /a-d')

def f_show_date():
	print_message('Showing current date and time')
	os.system('date /T')
	os.system('time /T')

## MAIN
print_message('Starting')


beInLoop    = True
prompt      = 'PyCLI # >' 

while beInLoop:
	try:
		print(prompt+' ', end='', flush=True)
		cli_input = get_input()
		print()
		if cli_input == 'exit':
			print_message('Exiting')
			sys.exit()

		isValid, func = isValidCmd(cli_input)
		
		if isValid:     
			str_to_class(func)()
		else:
			print('Invalid command : {}'.format(func))

	except KeyboardInterrupt:
		print_message("Exiting")
		sys.exit()