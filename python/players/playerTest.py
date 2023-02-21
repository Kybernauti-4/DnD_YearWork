import os
import players
import player_scripts.attack


p1_file = os.path.join(os.path.dirname(__file__), 'player_f436c19c.json')
p2_file = os.path.join(os.path.dirname(__file__), 'player_68acf1c9.json')


p1 = players.Player(p1_file)
p2 = players.Player(p2_file)

p1.usedItem(p1.equiped[0])
p1.save()
p2.usedItem(p2.equiped[0])
p2.save()