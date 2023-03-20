import importlib
import os
import sys
from time import sleep

import fileHandler
import stack

#! Handler is more or less done but a lot still isn't

#! &0 = current path
#! &1 = storyStack
#! &2 = playerlist
#! &3 = story_index
#! &4 = duunno for now
#! &5 = event_index 

npc_list = []
item_list = []
playerlist = []
valueStack = stack.listStack() #* The global stack that will be used
storyStack = []


#* import section
# create a list of locations of the scripts
scripts_path = {}
root_story_path = {}
# first try to find the story folder
i = 1 # used if there are multiple stories
for root, directories, files in os.walk(os.getcwd()):
	for filename in files:
		if filename == '_story.txt':
			root_story_path[i] = root
			i += 1

# let the user choose if there are multiple stories
# print(root_story_path)
if len(root_story_path) > 1:
	print('Multiple stories found, please choose one:')
	for index, path in root_story_path.items():
		print('{}) {}'.format(index, path))
	try:
		choice = int(input('Choice: '))
	except:
		print('Invalid choice, please use a number next time')
		exit()
	
	root_story_path = root_story_path[choice]
else:
	root_story_path = root_story_path[1]

# then find the scripts
i = 1 # the index of the script location, recreating original file structure which was {1:'script_location_1', 2:'script_location_2', ...}
for root, directories, files in os.walk(root_story_path):
	for filename in files:
		if filename == '_scripts.txt':
			scripts_path[i] = root
			i += 1
			break

# preparing values for the import
event_scripts_list = [] 
info = {'id':{},'info':{}}

for index,path in scripts_path.items():
	import_path = os.path.join(os.getcwd(),path) # create the import path in relation to runtime location
	sys.path.insert(int(index), import_path) # insert the path into the sys.path list so we can import from it
	for event in os.listdir(import_path):
		if os.path.isfile(os.path.join(import_path, event)) and '.py' in event: # check if it is a file and if it is a python file
			event_scripts_list.append(event.replace('.py','')) # add the event to the list of events
		if 'info.json' in event: # handling of the info.json file
			pure_info = fileHandler.read(os.path.join(import_path, event)) # read the info.json file
			# the info file has to include a id and info section
			# nested sections are allowed in the info section
			for key,value in pure_info['id'].items(): 
				info['id'][key] = value
			for info_type in pure_info['info']:
				if info_type not in info['info']:
					info['info'][info_type] = []
				for value in pure_info['info'][info_type]:
					info['info'][info_type].append(value)
			
# when I have the list of scripts and event that I need I can actually import them
import_list = []
#print(event_scripts_list)
for event in event_scripts_list:
	module = importlib.import_module(event)
	import_list.append(module)

# create a dictionary with the structure {event:imported_module}
#print(import_list)
imports = dict(zip(event_scripts_list, import_list))
#for import_key,import_name in imports.items():
#	print("Imported: {} => {}".format(import_key, import_name))

#* end of import section

#* Handler section
def addressReplace(arguments_in):
	"""A subsection of handle that replaces &id with the value of that id from memory

	Args:
		arguments_in (list): a list of arguments that will be passed to the function

	Returns:
		list: a list with replaced values, with the list the function can be called
	"""
	stack = valueStack.getValue()
	arguments = arguments_in.copy()
	for arg in arguments:
		try:
			if '&' in arg: # check if I am asking for address
				id = arg.replace('&','') # get the numeric address
				for value in stack: # search stack for that address which is always at [1] in element
					if value[1] == int(id): # if found
						arguments[arguments.index(arg)] = value[0] # assign that value to replace the adress
						if int(id) not in info['info']['lock']: # if the value is not locked
							valueStack.pop(stack.index(value)) # remove it from the stack
		except:
			pass
	
	return arguments

def handle(event_string, arguments_in):
	"""This function is used to call events (their respective functions) and pass on arguments, 
	when the function ends, handle will try to either save the return value to memory, or in case of logic functions,
	it will modify the current event file to include the new events

	Args:
		event_string (str): event name, doesn't include the last part of the file name (_X where X is the index)
		arguments_in (list): raw list of arguments as is in the event file, address replace will handle memory manipulation
	"""

	#print("Handling: {} => {}".format(event_string, arguments))
	#input('Press enter to continue')
	arguments = addressReplace(arguments_in)

	event_string_id = info['id'][event_string] # get the id of the event
	
	if event_string_id in info['info']['func']: # if the event is a function
		function = getattr(imports[event_string],event_string) # get the function from the file
		#print(arguments)
		return_value = function(*arguments) # run the function and unpack the argument list into the arguments
		if return_value != None:
			if type(return_value) == dict:
				for raw_key,val in return_value.items():
					if '_' in raw_key: 
						key = '_'.join(raw_key.split('_')[:-1])
					else:
						key = raw_key
					if key in list(imports.keys()):
						function = getattr(imports['addEvent'], 'addEvent')
						function(getValue(0), key, val)
					elif key == 'self' and val == 'true':
						function = getattr(imports['addEvent'], 'addEvent')
						function(getValue(0), event_string, arguments_in)
					elif key.endswith('.json'):
						events_to_add = fileHandler.read(os.path.join(getValue(0), 'event_collections',  key))
						for raw_event, args in events_to_add.items():
							function = getattr(imports['addEvent'], 'addEvent')
							if '_' in raw_event:
								event = '_'.join(raw_event.split('_')[:-1])
							else:
								event = raw_event
							function(getValue(0), event, args)
					else:
						valueStack.append([return_value,event_string_id]) # if the function returns a value, add it to the stack
			else:
				valueStack.append([return_value,event_string_id])

	elif event_string_id in info['info']['obj']: # if the event is an object
		obj = getattr(imports[event_string],event_string) # get the object from the file
		use_obj = obj(*arguments) # create the object and unpack the argument list into the constructor arguments
		valueStack.append([use_obj,event_string_id]) # add the object to the stack

#* End of handler section

#* helper functions
#used more or less just for getting values into variables in the main loop
def getValue(id):
	"""You can find this function inside the stack object definition

	Args:
		id (str or int): the id of the value you want to get

	Returns:
		any: the value of the id
	"""
	stack = valueStack.getValue()
	for value in stack:
		if value[1] == int(id):
			return_val = value[0]
			if int(id) not in info['info']['lock']:
				valueStack.pop(stack.index(value))
			return return_val
#* End of helper functions

#* Garbage collector
def garbageCollector():
	"""Used only to clean up the stack, it removes all values that are not locked, should be used at the end of story part
	"""
	stack = valueStack.getValue()
	for value in stack:
		if int(value[1]) not in info['info']['lock']:
			valueStack.pop(stack.index(value))
#* End of garbage collector

#* The main loop
if __name__ == "__main__":
	valueStack.append([root_story_path,0])
	init_events = fileHandler.read(os.path.join(root_story_path,'init.json')) # read the init file

	#handle all init events
	for event,args in init_events.items():
		try:
			#print("Handling: {} => {}".format(event, args))
			handle(event,args)
		except Exception as e:
			#print("Error in init event: {} => {}".format(event, e))
			pass

	#get the runtime vars for use in the main loop
	playerlist = getValue(7)
	storyStack = getValue(10)
	event_index = 0
	story_index = 0
	#print('Init events done')
	#print('Playerlist: {}'.format(playerlist))

	#create list of defaults the defaults with correct values
	#the 0 index is reserved for story_path
	default_values = {
		1:storyStack,
		2:playerlist,
		3:story_index,
		4:event_index,
		5:root_story_path
	}


	# upload runtime vars to the value stack
	for index,default in default_values.items():
		valueStack.append([default,index])
			

	#now we have the actual paths for the story parts so we can go to main loop
	while True:
		#update runtime vars, this allows for live changes to the events
		story_index = getValue(3)
		storyStack = getValue(1)
		story_part = storyStack[story_index]
		#overwrite the story_path value in the stack to the actual story part
		valueStack.setValueByID(0,story_part)
	
		#actual events loop inside the story parts
		valueStack.setValueByID(4,0)
		while True:
			#again, this loop is made to allow for dynamic changes to the events
			#update event_index
			event_index = getValue(4)

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
			if '_' in event:
				event = '_'.join(event.split('_')[:-1])

			#handle the event
			if event == 'input' and arg == 'None' and len(storyStack) <= story_index+1: # input:none is returned by storyHandler when he cannot find the correct file
				#print('Breaking out of main loop')
				window = getValue(9)
				window.add_text('The story has ended')
				window.stop_auto_render()
				exit()
			else:
				handle(event,arg)

			#update event_index
			valueStack.setValueByID(4,event_index+1)
			
		
		valueStack.setValueByID(3,story_index+1)
		#garbageCollector()