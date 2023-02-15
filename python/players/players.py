import json
import random
import os

class Player:
	
	def __init__(self, PlayerFile):
		PlayerData = {}

		with open(PlayerFile) as f:
			PlayerData	= json.load(f)
		
		if PlayerData['type'] != 'player':
			raise Exception('This is not a player file')
		
		self.pid = PlayerData["ID"]
		if self.pid == '':
			self.pid = ''.join([random.choice('0123456789abcdef') for i in range(8)]) # u32
		
		self.info = PlayerData["info"]
		self.inventory = PlayerData["inventory"]
		self.equiped = PlayerData["equiped"]

		
	def getVar(self, var):
		return self.info[var]

	def setVar(self, var):
		self.info[var] = var
	
	def getHit(self, damage):
		self.info["HP"] -= damage

	def equip(self, item):
		if item['type'].split('-')[0] == 'weapon':
			self.inventory.append(self.equiped[0])
			self.equiped[0] = item
			self.inventory.remove(item)
		elif item['type'].split('-')[0] == 'armor':
			self.inventory.append(self.equiped[1])
			self.equiped[1] = item
			self.inventory.remove(item)
		else:
			raise Exception('Invalid item type')

	def unequip(self, item):
		if item['type'].split('-')[0] == 'weapon':
			self.inventory.append(self.equiped[0])
			self.equiped[0] = None
		elif item['type'].split('-')[0] == 'armor':
			self.inventory.append(self.equiped[1])
			self.equiped[1] = None
		else:
			raise Exception('Invalid item type')

	def addItem(self, item):
		total_weight = 0
		for i in self.inventory:
			total_weight += i['weight']
		if total_weight + item['weight'] > self.info['Carry']:
			raise Exception('Inventory full')
		else:
			self.inventory.append(item)
	
	def removeItem(self, item):
		self.inventory.remove(item)

	def usedItem(self, item):
		item['Durability'] -= item['Usage']['Durability']
		if item['uses'] <= 0:
			self.inventory.remove(item)

	def save(self):

		PlayerData = {}
		PlayerData["ID"] = self.pid
		PlayerData["type"] = "player"
		PlayerData["player_info"] = self.info
		PlayerData["inventory"] = self.inventory
		
		with open((os.path.dirname(__file__) + self.pid + '.json'), 'w') as f:
			json.dump(PlayerData, f, indent=4)

#def all_equal(interator):
#	iterator = iter(iterator)
#	try:
#		first = next(interator)
#	except StopIteration:
#		return True
#	return all(first == x for x in iterator)
