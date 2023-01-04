import json
import os
from time import sleep

import comm
import deviceHandler
import fileHandler
import storyHandler
import story.events_scripts.Window as Window

#TODO Create a game body

npc_list = []
item_list = []
playerlist = []
story_path = os.path.join(os.getcwd(), 'story')
storyStack = storyHandler.get_storyparts(story_path)

window = Window.Window(64, 16)

folder = os.path.join(os.getcwd(), 'player')

def getPlayers(method):
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

for event in storyStack:
	npc_list = []
	txt_to_draw = fileHandler.read(os.path.join(event, 'storypart.txt'))
	try:
		npc_path = fileHandler.getFolder(event,'npc')
		npc_file_list = [file for file in os.listdir(npc_path)]
		for file in npc_file_list:
			npc_list.append(fileHandler.read(os.path.join(npc_path,file)))
	except:
		print("No NPC found")
	print(npc_list)
	#window.send_txt(txt_to_draw)