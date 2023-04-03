id = 'global'
name = ''

def getItem(p, ID):
	for item in p.inventory:
		if item['id'] == ID:
			return item
	for item in p.equipped:
		if item['id'] == ID:
			return item
	
	return None