import os
import players
import player_scripts.attack


p1_file = os.path.join(os.path.dirname(__file__), 'player.json')
p2_file = os.path.join(os.path.dirname(__file__), 'player2.json')


p1 = players.Player(p1_file)
p2 = players.Player(p2_file)

for piece in p1.equiped:
	print(f"p1 - equip: {piece['name']}")

for piece in p2.equiped:
	print(f"p2 - equip: {piece['name']}")