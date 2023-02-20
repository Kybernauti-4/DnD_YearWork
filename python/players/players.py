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
		type == item['type'].split('-')[0]
		if type != 'weapon' or type != 'armor':
			raise Exception('Invalid item type to equip')

		try:
			self.removeItem(item)
		except:
			raise 'Cannot equip item, not in inventory'

		match type:
			case 'weapon':
				try:
					self.addItem(self.equiped[0])
				except:
					self.addItem(item)
					raise 'Cannot unequip item, inventory full'

				self.equiped[0] = item

			case 'armor':
				try:
					self.addItem(self.equiped[1])
				except:
					self.addItem(item)
					raise 'Cannot unequip item, inventory full'

				self.equiped[1] = item


	def unequip(self, item):
		type == item['type'].split('-')[0]
		if type != 'weapon' or type != 'armor':
			raise Exception('Invalid item type to equip')
		
		if self.equiped[0] != item or self.equiped[1] != item:
			raise Exception('Item not equipped')

		try:
			self.addItem(item)
		except:
			raise 'Cannot unequip item, inventory full'
		
		match type:
			case 'weapon':
				self.equiped[0] = None
			case 'armor':
				self.equiped[1] = None

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
		in_inventory = False
		for i in self.inventory:
			if i == item:
				in_inventory = True
		
		if not in_inventory:
			raise Exception('Item not in inventory')

		item['Durability'] -= item['Usage']['Durability']
		if item['uses'] <= 0:
			self.inventory.remove(item)
			return 'Item destroyed'

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
