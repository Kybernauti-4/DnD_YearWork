id = 'global'
name = 'Show Equipment'

def getEquip(p, return_type='dict'):
	if return_type == 'list':
		equip_list = []
		for item in p.equipped:
			equip_list.append(item['name'])

		return equip_list

	elif return_type == 'dict':
		equip_dict = {}
		for item in p.equipped:
			equip_dict.append({item['name']: item})

		return equip_dict