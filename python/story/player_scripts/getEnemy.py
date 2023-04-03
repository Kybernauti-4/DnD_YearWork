import os
import json

id='global'
name=''

def getEnemy(path, return_type='dict'):
	npc_list = os.listdir(os.path.join(path, 'npc'))
	
	if return_type == 'list':
		enemy_list = []
		for npc in npc_list:
			with open(os.path.join(path, 'npc', npc), 'r') as f:
				npc_data = json.load(f)
				if npc_data['type'] == 'enemy':
					enemy_list.append(npc_data['info']['name'])
		
		return enemy_list
	
	elif return_type == 'dict':
		enemy_dict = {}
		for npc in npc_list:
			with open(os.path.join(path, 'npc', npc), 'r') as f:
				npc_data = json.load(f)
				if npc_data['type'] == 'enemy':
					enemy_dict[npc_data['info']['name']] = npc_data['ID']
		
		return enemy_dict
	

if __name__ == '__main__':
	print(getEnemy('story//Chapter_1//Encounter_1//Scene_1', 'list'))
	print(getEnemy('story//Chapter_1//Encounter_1//Scene_1', 'dict'))