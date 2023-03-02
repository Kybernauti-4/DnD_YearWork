id = 'global'
name = 'Get Equipment'

def getEquip(p, return_type='list'):
	if return_type == 'list':
		equip_list = []
		for item in p.equiped:
			equip_list.append(item['name'])

		return equip_list

	elif return_type == 'dict':
		equip_dict = {}
		for item in p.equiped:
			equip_dict.append(item['name'])

		return equip_dict