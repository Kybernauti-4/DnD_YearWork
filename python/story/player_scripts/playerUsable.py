import importlib
import os
import sys

id = 'global'
name = ''

def playerUsable(p):
	usable_scripts = {}

	if p.info['status'] == 'dead':
		return {'Dead': None}

	for script in os.listdir('story/player_scripts'):
		if not script.endswith('.py'):
			continue

		if script == __file__:
			continue
		
		sys.path.append('story/player_scripts')
		script = importlib.import_module(script[:-3])
		if script.id == 'global' or script.id == p.pid:
			if script.name != '':
				usable_scripts[script.name] = script
	
	return usable_scripts