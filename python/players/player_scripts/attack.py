unique_pid = 'global'

def attack(p1, p2, bufs):
	# p1 is the attacker
	weapon = None
	for item in p1.equipped:
		if item['type'].split('-')[0] == 'weapon':
			weapon = item
			break

	if weapon == None:
		damage = 1
	else:
		damage = weapon['damage']
	
	if weapon['type'].split('-')[1] != 'magic':
		for item in p2.equipped:
			if item['type'].split('-')[0] == 'armor':
				damage -= item['Defense']
	
	if damage < 0:
		damage = 0
	
	p2.getHit(damage)
	p1.usedItem(weapon)

