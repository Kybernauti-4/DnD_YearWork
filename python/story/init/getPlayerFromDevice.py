import deviceHandler
import comm
import os
import json
import fileHandler


def getPlayersFromDevice(method, folder):
	playerlist =[]
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

	return playerlist