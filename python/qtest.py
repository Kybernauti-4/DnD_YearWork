import os
import json

with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r') as f:
	file_content = json.load(f)

screen = []


print(screen)