import json
import os
import random


class Enemy:
	
	def __init__(self, path, EnemyID):
		EnemyData = {}
		for file in os.listdir(os.path.join(path,'npc')):
			if file.endswith('.json'):
				with open(os.path.join(path,'npc',file)) as f:
					EnemyData = json.load(f)
					if EnemyData['ID'] == EnemyID and EnemyData['type'] == 'enemy':
						break
		
		self.path = path
		self.pid = EnemyID
		if self.pid == '':
			self.pid = ''.join([random.choice('0123456789abcdef') for i in range(16)]) # u64
		
		self.info = EnemyData["info"]
		self.inventory = EnemyData["inventory"]
		self.equipped = EnemyData["equipped"]

		
	def getVar(self, var):
		return self.info[var]

	def setVar(self, var):
		self.info[var] = var
	
	def getHit(self, damage):
		self.info["HP"] -= damage
		if self.info["HP"] <= 0:
			self.info["HP"] = 0
			self.info['status'] = 'dead'
		if self.info["HP"] > self.info["max_HP"]:
			self.info["HP"] = self.info["max_HP"]

	def equip(self, item):
		type = item['type'].split('-')[0]
		if type != 'weapon' and type != 'shield':
			raise Exception('Invalid item type to equip')

		try:
			self.removeItem(item)
		except:
			raise 'Cannot equip item, not in inventory'

		match type:
			case 'weapon':
				try:
					self.addItem(self.equipped[0])
				except:
					self.addItem(item)
					raise 'Cannot unequip item, inventory full'

				self.equipped[0] = item

			case 'shield':
				try:
					self.addItem(self.equipped[1])
				except:
					self.addItem(item)
					raise 'Cannot unequip item, inventory full'

				self.equipped[1] = item


	def unequip(self, item):
		type = item['type'].split('-')[0]
		if type != 'weapon' and type != 'shield':
			raise Exception('Invalid item type to equip')
		
		if self.equipped[0] != item and self.equipped[1] != item:
			raise Exception('Item not equipped')

		try:
			self.addItem(item)
		except:
			raise 'Cannot unequip item, inventory full'
		
		match type:
			case 'weapon':
				self.equipped[0] = None
			case 'shield':
				self.equipped[1] = None

	def addItem(self, item):
		total_weight = 0
		for i in self.inventory:
			total_weight += i['weight']
		if total_weight + item['weight'] > self.info['carry']:
			raise Exception('Inventory full')
		else:
			self.inventory.append(item)
	
	def removeItem(self, item):
		self.inventory.remove(item)

	def usedItem(self, item):
		available = False
		for i in self.inventory:
			if i == item:
				available = True

		for i in self.equipped:
			if i == item:
				available = True
		
		if not available:
			raise Exception('Item not in inventory')

		item['durability'] -= item['usage']['durability']
		if item['durability'] <= 0:
			self.inventory.remove(item)
			return 'Item destroyed'

	def save(self):

		PlayerData = {}
		PlayerData["ID"] = self.pid
		PlayerData["type"] = "player"
		PlayerData["info"] = self.info
		PlayerData["equipped"] = self.equipped
		PlayerData["inventory"] = self.inventory
		
		with open(os.path.join(self.path, "npc", f'enemy_{self.pid}.json'), 'w') as f:
			json.dump(PlayerData, f, indent=4)
