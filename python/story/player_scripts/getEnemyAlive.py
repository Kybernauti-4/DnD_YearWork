import json

id = 'global'
name = ''

def getEnemyAlive(enemy_dict):
	alive_list = []
	for enemy in enemy_dict:
		if enemy['info']['status']=='alive':
			alive_list.append(enemy)

	return alive_list