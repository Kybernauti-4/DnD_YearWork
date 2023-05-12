import os
import json

def add_text(path,*args):
	window = args[0]
	autorender = args[1]
	args = args[2:]
	texts = []
	for arg in args:
		try:
			if arg.endswith('.txt'):
				texts.append(open(os.path.join(path,'texts',arg), 'r').read())
			else:
				texts.append(arg)
		except:
			#texts.append(str(path))
			if type(arg) == dict:
				for val in list(arg.values()):
					name = val['name']
					texts.append(f'{name}')
					keys = ["durability","damage","weight"]
					for key in keys:
						try:
							texts.append(f' - {key}: {val[key]}')
						except:
							pass

			else:
				texts.append(str(arg))

	for text in texts:
		if type(text) == str:
			window.add_text(text)
		elif type(text) == list:
			for line in text:
				window.add_text(line)
		if not autorender:
			window.format_render()
			window.show()