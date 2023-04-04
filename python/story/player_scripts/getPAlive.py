id = 'global'
name = ''

def getPAlive(playerList):
	dict = {}
	for player in playerList:
		if player.info['status'] == 'alive':
			dict[player.info['name']] = player
	
	return dict