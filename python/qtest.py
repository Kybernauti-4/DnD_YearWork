import re

s = 'print_1'

if match := re.search('_[0-9]+', s):
	print(match.group(0))
else:
	print('not found')