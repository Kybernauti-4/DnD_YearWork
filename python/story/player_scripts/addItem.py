import json
import os

id = 'global'
name = ''

def addItem(path, p1, item_str):
	item_to_add = {}
	os.chdir(os.path.join(path, "item_data"))
	for file in os.listdir():
		if file == f"{item_str}.json":
			with open(file, "r") as f:
				item_to_add = json.load(f)


	print(item_to_add)

	item_ID = 0
	for item in p1.equiped:
		if int(item['ID']) > item_ID:
			item_ID = int(item['ID'])
	
	for item in p1.inventory:
		if int(item['ID']) > item_ID:
			item_ID = int(item['ID'])
	
	item_ID += 1
	item_to_add['ID'] = item_ID

	try:
		p1.addItem(item_to_add)
		return 'Item added'
	except:
		return 'Inventory full'
