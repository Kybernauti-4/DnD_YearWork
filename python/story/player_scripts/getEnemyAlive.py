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
		for enemy, id in enemy_dict.items():
			if enemy_dict[enemy]['info']['status']=='alive':
				alive_dict[enemy]['info']['name'] = enemy_dict[enemy]
		return alive_dict
	