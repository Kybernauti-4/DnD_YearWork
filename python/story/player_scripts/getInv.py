id = 'global'
name = 'Show Inventory'

def getInv(p, return_type='list'):
	if return_type == 'list':
		inv_list = []
		for item in p.inventory:
			inv_list.append(item['name'])

		return inv_list
		
	elif return_type == 'dict':
		inv_dict = {}
		i = 0
		for item in p.inventory:
			inv_dict[item["name"]] = item
			i+=1

		return inv_dict