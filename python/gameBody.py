import importlib
import os
import sys

import fileHandler
import stack
import re

#TODO Create a game body
#TODO Create a smart garbage collector
#! Handler is more or less done but a lot still isn't
#TODO Comment handler (Kill me now)

#! &0 == current path

npc_list = []
item_list = []
playerlist = []
valueStack = stack.listStack() #* The global stack that will be used
storyStack = stack.listStack()

#* import loop
scripts_path = fileHandler.read('scriptlocation.json')

event_scripts_list = []

info = {'id':{},'info':{}}

for index,path in scripts_path.items():
	import_path = os.path.join(os.getcwd(),path)
	sys.path.insert(int(index),import_path)
	for event in os.listdir(import_path):
		if os.path.isfile(os.path.join(import_path, event)) and '.py' in event: 
			event_scripts_list.append(event.replace('.py',''))
		if 'info.json' in event:
			pure_info = fileHandler.read(os.path.join(import_path, event))
			for key,value in pure_info['id'].items():
				info['id'][key] = value
			for info_type in pure_info['info']:
				if info_type not in info['info']:
					info['info'][info_type] = []
				for value in pure_info['info'][info_type]:
					info['info'][info_type].append(value)
			
import_list = []
#print(event_scripts_list)
for event in event_scripts_list:
	module = importlib.import_module(event)
	import_list.append(module)

#print(import_list)
imports = dict(zip(event_scripts_list, import_list))
#for import_key,import_name in imports.items():
#	print("Imported: {} => {}".format(import_key, import_name))

def handle(event_string, arguments):
	stack = valueStack.getValue()
	for arg in arguments:
		if '&' in str(arg):
			id = arg.replace('&','')
			for value in stack:
				if value[1] == int(id):
					arguments[arguments.index(arg)] = value[0]
					if int(id) not in info['info']['lock']:
						valueStack.pop(stack.index(value))

	event_string_id = info['id'][event_string]
	
	if event_string_id in info['info']['func']:
		function = getattr(imports[event_string],event_string)
		return_value = function(*arguments)
		if return_value != None:
			valueStack.append([return_value,event_string_id])

	elif event_string_id in info['info']['obj']:
		obj = getattr(imports[event_string],event_string)
		use_obj = obj(*arguments)
		valueStack.append([use_obj,event_string_id])

#* used more or less just for getting values into variables in the main loop
def getValue(id):
	stack = valueStack.getValue()
	for value in stack:
		if value[1] == int(id):
			return_val = value[0]
			if int(id) not in info['info']['lock']:
				valueStack.pop(stack.index(value))
			return return_val

def garbageCollector():
	stack = valueStack.getValue()
	for value in stack:
		if int(value[1]) not in info['info']['lock']:
			valueStack.pop(stack.index(value))

#* The main loop
if __name__ == "__main__":
	#* First we go through init events and then we go through the story
	player_folder = os.path.join(os.getcwd(), 'players')
	story_path = os.path.join(os.getcwd(), 'story')
	valueStack.append([story_path,0])
	init_events = fileHandler.read(os.path.join(os.getcwd(),'story','init.json'))

	for event,args in init_events.items():
		try:
			#print(event,args)
			handle(event,args)
		except Exception as e:
			print("Error in init event: {} => {}".format(event, e))
			

	#now we have the actual paths for the story parts so we can go to main loop
	story_parts = getValue(5)
	for story_part in story_parts:
		valueStack.setValueByID(0,story_part)
		story_events = fileHandler.read(os.path.join(story_part,'events.json'))
		#print(story_events)
		for event,args in story_events.items():
			if match := re.search('_[0-99]+', event):
				event = event.replace(match.group(0),'')
			print(event,args)
			input()
			handle(event,args)
		#garbageCollector()