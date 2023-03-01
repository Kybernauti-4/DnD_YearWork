import deviceHandler
import comm
import os
import json
from Player import Player


def getPlayerList(folder):
	playerlist =[]
	try:
		devicesList = deviceHandler.findDevices()
	except: devicesList = []

	players = os.listdir(folder)
	for player in players:
		try:
			p = Player(os.path.join(folder, player))
			playerlist.append(p)
		except:
			pass

	for device in devicesList:
		comm.sendMessage(device, 'sendpdata')
		player_data = json.loads(comm.readMessageBlock(player, True))
		with open(os.path.join(folder, 'temp.json'), 'w') as f:
			json.dump(player_data, f)
			try:
				p = Player(os.path.join('story\\players', 'temp.json'))
				p.save()
				playerlist.append(p)
			except:
				pass
			os.remove(os.path.join(folder, 'temp.json'))
				
	return playerlist


if __name__ == '__main__':
	player_path = os.path.join('story\\players')
	print(plist := getPlayerList(player_path))
	print(plist[0].info)