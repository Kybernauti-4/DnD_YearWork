def match(input, keys, values):
	for key in keys:
		if input == key:
			return values[keys.index(key)]
