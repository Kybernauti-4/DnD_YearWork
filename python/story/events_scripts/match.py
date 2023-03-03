from addEvent import addEvent


def match(path, input, keys, values):
	for key in keys:
		if input == key:
			work_key = key
			work_val = values[keys.index(key)]

	if work_val == '':
		return
	
	if work_key.endswith('.py'):
		addEvent(path, work_key.replace('.py', ''))