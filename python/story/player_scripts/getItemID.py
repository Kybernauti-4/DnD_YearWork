id = 'global'
name = ''

def getItemID(p, item):
	if item in p.inventory or item in p.equipped:
		try:
			return p.inventory.index(item)
		except:
			return p.equipped.index(item)
