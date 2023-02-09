import json
import random

#This is the first general file

class Player:
	
	def __init__(self, PlayerFile):
		PlayerData = {}

		with open(PlayerFile) as f:
			PlayerData	= json.load(f)
		
		if PlayerData['type'] != 'player':
			raise Exception('This is not a player file')
		
		self.pid = PlayerData["ID"]
		if self.pid == '':
			self.pid = ''.join(random.choice('0123456789abcdef'), 8) # u32
		
		self.player_info = PlayerData["player_info"]

		
	def getVar(self, var):
		return self.player_info[var]

	def setVar(self, var):
		self.player_info[var] = var
	
	def getHit(self, damage):
		self.player_info["HP"] -= damage

	def save(self):

		PlayerData = {}
		PlayerData["ID"] = self.pid
		PlayerData["type"] = "player"
		PlayerData["player_info"] = self.player_info
		
		with open(self.pid + '.json', 'w') as f:
			json.dump(PlayerData, f, indent=4)

#def all_equal(interator):
#	iterator = iter(iterator)
#	try:
#		first = next(interator)
#	except StopIteration:
#		return True
#	return all(first == x for x in iterator)
