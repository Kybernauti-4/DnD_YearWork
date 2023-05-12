import json

id = 'global'
name = ''

def getEnemyAlive(enemy_dict, type = 'dict'):
	if type == 'list':
		alive_list = []
		for enemy in enemy_dict:
			if enemy['info']['status']=='alive':
				alive_list.append(enemy)
		return alive_list
	if type == 'dict':
		alive_dict = {}
		for name, enemy in enemy_dict.items():
			if enemy.info['status']=='alive':
				alive_dict[name] = enemy

		if True:
			pass
		return alive_dict
	