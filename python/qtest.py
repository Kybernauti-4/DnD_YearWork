import os
import json
import keyboard



def update_variable(e, vertical, screen, line):
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
		line = curr_line
		print(f'\r\u001b[33m{curr_line}\u001b[0m', end='', flush=True)
		down_num = len(screen) - vertical[0]
		print(f'\r\u001b[{down_num}B{curr_line.strip()}', end='', flush=True)

with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r') as f:
	file_content = json.load(f)


vertical = [0]

screen = []
curr_line = ''
bracket_check = False
for index,char in enumerate(json.dumps(file_content, indent=4)):
	if char == '[':
		bracket_check = True
	elif char == ']':
		bracket_check = False

	if char == '\n' and not bracket_check:
		screen.append(curr_line)
		curr_line = ''
		continue

	if bracket_check:
		if char == ' ':
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

line = ''

keyboard.on_press(lambda e: update_variable(e, vertical, screen))
keyboard.wait()