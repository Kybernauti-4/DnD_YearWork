import os
import json

with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r') as f:
	file_content = json.load(f)

screen = []
curr_line = ''
for char in json.dumps(file_content, indent=4):
	if char == '\n':
		screen.append(curr_line)
		curr_line = ''
		continue
	curr_line += char

print(screen)