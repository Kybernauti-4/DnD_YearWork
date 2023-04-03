def getPDict(playerList):
	dict = {}
	for player in playerList:
		dict[player.info['name']] = player
	
	return dict