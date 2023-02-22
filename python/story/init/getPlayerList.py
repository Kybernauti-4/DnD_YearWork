import deviceHandler
import comm
import os
import json


def getPlayerList(folder):
	playerlist =[]
	try:
		devicesList = deviceHandler.findDevices()
		for player in devicesList:
			comm.sendMessage(player, 'sendpdata')
			playerlist.append(json.loads(comm.readMessageBlock(player, True)))
	except:
		players = os.listdir(folder)
		for player in players:
			with open(os.path.join(folder, player), 'r') as f:
				playerlist.append(json.load(f))
	
	if len(playerlist) == 0:
		players = os.listdir(folder)
		for player in players:
			with open(os.path.join(folder, player), 'r') as f:
				playerlist.append(json.load(f))
		
	return playerlist


if __name__ == '__main__':
	player_path = os.path.join('story', 'players')
	print(plist := getPlayerList(player_path))
	print(plist[0]['info']['name'])