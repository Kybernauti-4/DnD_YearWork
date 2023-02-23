def usePot(player, pot):
	if pot not in player.inventory:
		raise Exception('Item not in inventory')
	try:
		effects = pot['effects']
	except:
		raise Exception('Item has no effects')

	player.usedItem(pot)
	
	for effect in effects:
		player.info[effect] += effects[effect]