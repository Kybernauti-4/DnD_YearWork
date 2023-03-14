id = 'global'
name = ''

def removeItem(player, item_ID):
	item_to_remove = {}
	for item in player.inventory:
		if item['ID'] == item_ID:
			item_to_remove = item
			break

	if item_to_remove == {}:
		return 'Item not found or is equipped'
	
	player.removeItem(item_to_remove)
	return 'Item removed'