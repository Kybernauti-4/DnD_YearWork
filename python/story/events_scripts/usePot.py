def usePot(pot,player):
	try:
		effects = pot['effects']
	except:
		raise Exception('Item has no effects')

	player.usedItem(pot)
	
	for effect in effects:
		player.info[effect] += effects[effect]