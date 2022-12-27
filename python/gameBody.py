import comm
import deviceHandler
import json
import fileHandler
import os
import storyHandler
import Window

#TODO Create a game body

#? I need to implement an event stack that advances each round
#* Create a list of players either through comm or through searching in files
playerlist = []
story_path = os.path.join(os.getcwd(), 'story')
storyStack = storyHandler.get_storyparts(story_path)

window = Window.Window(256, 16)

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
	txt_to_draw = fileHandler.read(os.path.join(event, 'storypart.txt'))
	window.draw(txt_to_draw)
