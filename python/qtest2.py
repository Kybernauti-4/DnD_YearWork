import os

path = os.path.dirname(__file__)
new_path = ''
path_parts = path.split('\\')
print(path_parts)
if 'python' in path_parts:
	index = path_parts.index('python')
	new_path = '/'.join(path_parts[:index+1])
else:
	print(f"python not found in {path}")

print(new_path)