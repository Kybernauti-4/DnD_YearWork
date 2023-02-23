from story.init.Player import Player
from story.events_scripts.usePot import usePot
import os

player = Player(os.path.join('story', 'players', 'player_723fad5158658785.json'))

for item in player.inventory:
	if item['type'] == 'potion':
		usePot(player, item)
		break

print(player.info)
print(player.inventory)