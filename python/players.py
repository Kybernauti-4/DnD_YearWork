import json

#This is the first general file

class Player:
	
	def __init__(self, PlayerData):
		self.HP = PlayerData['HP']
		self.MP = PlayerData['MP']
		self.Name = PlayerData['Name']
		self.Age = PlayerData['Age']
		self.Gender = PlayerData['Gender']
		
f = open('player.json')

player_data = json.load(f)
Giganto = Player(player_data["player info"][0])

f.close()
print(Giganto.HP)

def all_equal(interator):
	iterator = iter(iterator)
	try:
		first = next(interator)
	except StopIteration:
		return True
	return all(first == x for x in iterator)

#def assignID():
#	with open('playerlist.json') as list:
#		player_list = list['player_list']
#		for player in list:			 