import os

def add_text(path,*args):
	texts = []
	for arg in args:
		if arg.endswith('.txt'):
			texts.append(open(os.path.join(path,'texts',arg), 'r').read())
		else:
			texts.append(arg)
	return texts