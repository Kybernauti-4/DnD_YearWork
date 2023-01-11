import importlib
import json
import os
import sys
from time import sleep

import fileHandler
import story.init.comm as comm
import story.init.deviceHandler as deviceHandler
import story.init.Window as Window
import storyHandler
import stack

#TODO Create a game body
#TODO Create a smart garbage collector
#! Handler is more or less done but a lot still isn't
#TODO Comment handler (Kill me now)

#! &0 == current path

npc_list = []
item_list = []
playerlist = []
valueStack = stack.listStack() #* The global stack that will be used
story_path = os.path.join(os.getcwd(), 'story')
storyStack = stack.listStack()
for part in storyHandler.get_storyparts(story_path):
	storyStack.append(part)

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
	#print("Imported: {} => {}".format(import_key, import_name))

def handle(event_string, arguments):
	for arg in arguments:
		if '&' in str(arg):
			id = arg.replace('&','')
			for value in valueStack.getList():
				if value[1] == int(id):
					arguments[arguments.index(arg)] = value[0]
					if int(id) not in info['info']['lock']:
						valueStack.pop(valueStack.getList().index(value))
	event_string_id = info['id'][event_string]
	if event_string_id in info['info']['func']:
		function = getattr(imports[event_string],event_string)
		return_value = function(*arguments)
		if return_value != None:
			if type(return_value) == list:
				for value in return_value:
					valueStack.append([value,event_string_id])
			else:
				valueStack.append([return_value,event_string_id])

	elif event_string_id in info['info']['obj']:
		obj = getattr(imports[event_string],event_string)
		use_obj = obj(*arguments)
		valueStack.append([use_obj,event_string_id])

def garbageCollector():
	pass

player_folder = os.path.join(os.getcwd(), 'players')

valueStack.append([os.path.join(os.getcwd(),'story','Chapter_1','Encounter_1','Scene_1','texts'),0])


handle('Window', [64,30])
handle('add_text', ['&0','txt1.txt','txt2.txt'])
handle('print_text', ['&13', '&4'])
handle('print_text', ['&13', '&4'])

#getPlayers('files')
#print(playerlist)
#print(playerlist[0]['player_info']['Name'])

#for event in storyStack:
#	npc_list = []
#	txt_to_draw = fileHandler.read(os.path.join(event, 'storypart.txt'))
#	try:
#		npc_path = fileHandler.getFolder(event,'npc')
#		npc_file_list = [file for file in os.listdir(npc_path)]
#		for file in npc_file_list:
#			npc_list.append(fileHandler.read(os.path.join(npc_path,file)))
#	except:
#		print("No NPC found")
#	print(npc_list)
#	#window.send_txt(txt_to_draw)