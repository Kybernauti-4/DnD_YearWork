import importlib
import os
import re
import sys

import fileHandler
import stack

#! Handler is more or less done but a lot still isn't
#TODO Comment handler (Kill me now)

#! &0 = current path
#! &1 = storyStack
#! &2 = valueStack
#! &3 = story_index
#! &4 = playerlist
#! &5 = event_index 

npc_list = []
item_list = []
playerlist = []
valueStack = stack.listStack() #* The global stack that will be used
storyStack = []


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
	#print("Handling: {} => {}".format(event_string, arguments))
	#input('Press enter to continue')
	stack = valueStack.getValue()
	for arg in arguments:
		if '&' in str(arg): # check if I am asking for adress
			id = arg.replace('&','') # get the numeric adress
			for value in stack: # search stack for that addres which is always at [1] in element
				if value[1] == int(id): # if found
					arguments[arguments.index(arg)] = value[0] # assign that value to replace the adress
					if int(id) not in info['info']['lock']: # if the value is not locked
						valueStack.pop(stack.index(value)) # remove it from the stack

	event_string_id = info['id'][event_string] # get the id of the event
	
	if event_string_id in info['info']['func']: # if the event is a function
		function = getattr(imports[event_string],event_string) # get the function from the file
		#print(arguments)
		return_value = function(*arguments) # run the function and unpack the argument list into the arguments
		if return_value != None:
			valueStack.append([return_value,event_string_id]) # if the function returns a value, add it to the stack

	elif event_string_id in info['info']['obj']: # if the event is an object
		obj = getattr(imports[event_string],event_string) # get the object from the file
		use_obj = obj(*arguments) # create the objeck and unpack the argument list into the constructor arguments
		valueStack.append([use_obj,event_string_id]) # add the object to the stack

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
	#include globals
	#* First we go through init events and then we go through the story
	story_path = os.path.join(os.getcwd(), 'story')
	valueStack.append([story_path,0])
	init_events = fileHandler.read(os.path.join(os.getcwd(),'story','init.json'))

	for event,args in init_events.items():
		try:
			#print("Handling: {} => {}".format(event, args))
			handle(event,args)
		except Exception as e:
			#print("Error in init event: {} => {}".format(event, e))
			pass
	
	playerlist = getValue(7)
	storyStack = getValue(10)
	event_index = 0
	story_index = 0
	#print('Init events done')
	#print('Playerlist: {}'.format(playerlist))

	#create list of defaults the defaults with correct values
	default_values = {
		1:storyStack,
		2:playerlist,
		3:story_index,
		4:playerlist,
		5:event_index,
	}


	#After init, upload runtine vars to the value stack
	for index,default in default_values.items():
		valueStack.append([default,index])
			
	#print(storyStack)
	#now we have the actual paths for the story parts so we can go to main loop
	while True:
		story_index = getValue(3)
		storyStack = getValue(1)
		story_part = storyStack[story_index]
		valueStack.setValueByID(0,story_part)
		story_events = fileHandler.read(os.path.join(story_part,'events.json'))
		try:
			if story_events['input'] == 'None':
				#print('Breaking out of main loop')
				break
		except:
			pass
		#actual events inside the story parts
		valueStack.setValueByID(5,0)
		while True:
			#update event_index
			event_index = getValue(5)

			#update events to enable live adding of events
			story_events = fileHandler.read(os.path.join(story_part,'events.json'))
			
			#create list that can be accessed by event_index so that changes can be felt
			events = list(story_events.keys())
			args = list(story_events.values())

			#assign values to use in handle
			try:
				event = events[event_index]
				arg = args[event_index]
			except:
				#This means that there are no more events
				break

			#magic to get the pure event name without the index
			event = '_'.join(event.split('_')[:-1])

			#handle the event
			handle(event,arg)

			#update event_index
			valueStack.setValueByID(5,event_index+1)
			
		
		valueStack.setValueByID(3,story_index+1)
		#garbageCollector()