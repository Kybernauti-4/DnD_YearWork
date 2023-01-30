import os
import json
import keyboard



def update_variable(e, vertical, screen, line, context_menu, context, horizontal, cm_idx):
	if line[0]	== '':
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
			line[0] = curr_line.strip()
			horizontal[0] = len(line[0])


	else:
		if e.name == 'left' and len(context[0]) == 0:
			print(f'\u001b[D', end='', flush=True)
			horizontal[0] -= 1

		elif e.name == 'right' and len(context[0]) == 0:
			print(f'\u001b[C', end='', flush=True)
			horizontal[0] += 1
		
		elif e.name == 'up':
			if len(context[0]) > 0:
				print(f'\u001b[{len(context[0])}D\u001b[K', end='', flush=True)
				print(f'\u001b[34m{context_menu[cm_idx[0]]}\u001b[0m', end='', flush=True)
				print(f'{line[0][horizontal[0]:]}', end='', flush=True)
				context[0] = context_menu[cm_idx[0]] + line[0][horizontal[0]:]
				cm_idx[0] += 1
				if cm_idx[0] >= len(context_menu):
					cm_idx[0] = 0
				
			else:
				print(f'\u001b[34m{context_menu[cm_idx[0]]}\u001b[0m\u001b[K', end='', flush=True)
				print(f'{line[0][horizontal[0]:]}', end='', flush=True)
				context[0] = context_menu[cm_idx[0]] + line[0][horizontal[0]:]
				cm_idx[0] += 1
				if cm_idx[0] >= len(context_menu):
					cm_idx[0] = 0

		elif e.name == 'down':
			print(f'\r\u001b[K{line[0]}', end='', flush=True)
			horizontal[0] = len(line[0])
			cm_idx[0] = 0
			context[0] = ''

		elif e.name == 'tab':
			line[0] = line[0][:horizontal[0]] + context[0]
			print(f'\r\u001b[K{line[0]}', end='', flush=True)
			horizontal[0] = len(line[0])
			cm_idx[0] = 0
			context[0] = ''
		
		elif e.name == 'backspace' and len(context[0]) == 0:
			line[0] = line[0][:horizontal[0]-1] + line[0][horizontal[0]:]
			horizontal[0] -= 1
			print(f'\r\u001b[K{line[0]}', end='', flush=True)
			print(f'\r\u001b[{horizontal[0]}C', end='', flush=True)
		
		elif e.name == 'delete' and len(context[0]) == 0:
			line[0] = line[0][:horizontal[0]] + line[0][horizontal[0]+1:]
			print(f'\r\u001b[K{line[0]}', end='', flush=True)
			print(f'\r\u001b[{horizontal[0]}C', end='', flush=True)

		elif e.name == 'enter':
			

with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r') as f:
	file_content = json.load(f)


vertical = [0]

screen = []
curr_line = ''
bracket_check = False
string_check = False
for index,char in enumerate(json.dumps(file_content, indent=4)):
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

for i in range(len(screen)):
	if i != len(screen) - 1:
		print(screen[i])
	else:
		print(screen[i], end = '', flush=True)

vertical[0] = len(screen) - 1
horizontal = [0]

line = ['']
context_menu = ["[]", "{}", "\"\"", ":", "()"]
context = ['']
cm_idx = [0]

keyboard.on_press(lambda e: update_variable(e, vertical, screen, line, context_menu,context, horizontal, cm_idx))
keyboard.wait()