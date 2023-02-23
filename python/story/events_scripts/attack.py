def attack(p1, p2):
	# p1 is the attacker
	weapon = None
	for item in p1.equiped:
		if item['type'].split('-')[0] == 'weapon':
			weapon = item
			break

	if weapon == None:
		damage = 1
	else:
		damage = weapon['damage']
	#got damage from weapon now decrease it by armor unless its magic
	
	if weapon['type'].split('-')[1] != 'magic':
		for item in p2.equiped:
			if item['type'].split('-')[0] == 'shield':
				damage -= item['defense']
			elif item['type'].split('-')[0] == 'armor':
				damage -= item['defense']
	
	if damage < 0:
		damage = 0
	
	p2.getHit(damage)
	p1.usedItem(weapon)