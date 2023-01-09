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

#TODO Create a game body

npc_list = []
item_list = []
playerlist = []
story_path = os.path.join(os.getcwd(), 'story')
storyStack = storyHandler.get_storyparts(story_path)

#* import loop
scripts_path = fileHandler.read('scriptlocation.json')

event_scripts_list = []

for index,path in scripts_path.items():
	import_path = os.path.join(os.getcwd(),path)
	sys.path.insert(int(index),import_path)
	for event in os.listdir(import_path):
		if os.path.isfile(os.path.join(import_path, event)): 
			event_scripts_list.append(event.replace('.py',''))

import_list = []
for event in event_scripts_list:
	import_list.append(importlib.import_module(event.replace('.py','')))

imports = {keys:values for keys in event_scripts_list for values in import_list}

print(imports) 

def handle(event_string, arguments):
	function = getattr(imports[event_string],event_string)
	function(arguments)

window = Window.Window(256, 128)

folder = os.path.join(os.getcwd(), 'player')

def getPlayersFromDevice(method):
	match method:
		case 'device':
			devicesList = deviceHandler.findDevices()
			for player in devicesList:
				comm.sendMessage(player, 'sendpdata')
				playerlist.append(json.loads(comm.readMessageBlock(player, True)))
		case 'files':
			players = os.listdir(folder)
			for player in players:
				playerlist.append(fileHandler.read(os.path.join(folder, player)))

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