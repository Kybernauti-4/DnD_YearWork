from story.init.Player import Player
from story.player_scripts.addItem import addItem
from story.player_scripts.removeItem import removeItem

p = Player('story/players/player_00ca29e469c434dc.json')
path = 'story\\Chapter_1\\Encounter_1\\Scene_1'
print(addItem(path, p, 'bad_sword'))
removeID = ''
for item in p.inventory:
	if item['name'] == 'Bad Sword':
		removeID = item['ID']
		break

print(removeItem(p, removeID))
print(p.inventory)