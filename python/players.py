import json

#This is the first general file

class Player:
	
	def __init__(self, PlayerData):
		self.HP = PlayerData['HP']
		self.MP = PlayerData['MP']
		self.Name = PlayerData['Name']
		self.Age = PlayerData['Age']
		self.Gender = PlayerData['Gender']

	def getVariable(self, variable):
		match variable:
			case 'HP':
				return self.HP
			case 'MP':
				return self.MP
			case 'Name':
				return self.Name
			case 'Age':
				return self.Age
			case 'Gender':
				return self.Gender
				
	def setVariable(self, variable, new_value):
		match variable:
			case 'HP':
				self.HP = new_value
				return 1
			case 'MP':
				self.MP = new_value
				return 1
			case 'Name':
				self.Name = new_value
				return 1
			case 'Age':
				self.Age = new_value
				return 1
			case 'Gender':
				self.Gender = new_value
				return 1
		
	def attack(player, dmg_amount):
		player.getHit(dmg_amount)
	
	def getHit(dmg_amount):
		HP-=dmg_amount
		
f = open('player/player.json')

player_data = json.load(f)
Giganto = Player(player_data["player_info"])

f.close()

print(Giganto.HP)

#def all_equal(interator):
#	iterator = iter(iterator)
#	try:
#		first = next(interator)
#	except StopIteration:
#		return True
#	return all(first == x for x in iterator)

#def assignID():
#	with open('playerlist.json') as list:
#		player_list = list['player_list']
#		for player in list:			 