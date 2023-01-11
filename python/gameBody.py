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
#TODO Create a global stack for functions with id checks
#TODO Create a smart garbage collector
#TODO Finish the handling of functions and objects

npc_list = []
item_list = []
playerlist = []
valueStack = stack.dictStack() #* The global stack that will be used
story_path = os.path.join(os.getcwd(), 'story')
storyStack = stack.listStack()
storyStack.append(storyHandler.get_storyparts(story_path))

#* import loop
scripts_path = fileHandler.read('scriptlocation.json')

event_scripts_list = []

info = {'id':{},'info':{'func':[],'obj':[]}}

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
			for value in pure_info['info']['func']:
				info['info']['func'].append(value)
			for value in pure_info['info']['obj']:
				info['info']['obj'].append(value)
			
import_list = []
for event in event_scripts_list:
	import_list.append(importlib.import_module(event.replace('.py','')))

imports = {keys:values for keys in event_scripts_list for values in import_list}

#print(imports)
def handle(event_string, arguments):
	for arg in arguments:
		if '&' in arg:
			id = arg.replace('&','')
			for value in valueStack:
				if value[1] == id:
					arguments[index(arg)] = value[0]
	
	function = getattr(imports[event_string],event_string)
	function(*arguments)

window = Window.Window(256, 128)

folder = os.path.join(os.getcwd(), 'players')

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