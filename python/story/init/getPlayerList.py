import deviceHandler
import comm
import os
import json
from Player import Player


def getPlayerList(folder):
	playerlist =[]
	try:
		devicesDict = deviceHandler.findDevices()
	except: devicesDict = {}

	players = os.listdir(folder)
	for player in players:
		try:
			p = Player(os.path.join(folder, player))
			playerlist.append(p)
		except:
			pass

	for id,device in devicesDict.items():
		comm.sendMessage(device, 'sendpdata')
		player_data = json.loads((''.join(comm.readMessageBlock(device, True))).replace("'", '"'))
		#print(player_data)
		with open(os.path.join(folder, 'temp.json'), 'w') as f:
			json.dump(player_data, f, indent=4)
			#print('temp.json saved')
		try:
			p = Player(os.path.join('story\\players', 'temp.json'))
			print('Player created')
			p.save()
			print('Player saved')
			playerlist.append(p)
			print('Player added to list')
		except:
			print('Error in player creation')
			input()
			pass

		os.remove(os.path.join(folder, 'temp.json'))
				
	return playerlist


if __name__ == '__main__':
	player_path = os.path.join('story\\players')
	print(plist := getPlayerList(player_path))
	print(plist[0].info,'\n',plist[0].inventory,'\n',plist[0].equiped)
	print(plist[1].info,'\n',plist[1].inventory,'\n',plist[1].equiped)