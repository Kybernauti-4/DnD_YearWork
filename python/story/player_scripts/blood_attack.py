id = '00ca29e469c434dc'
name = 'Blood Attack'

fist = {
	"name": "Fist",
	"type": "weapon-melee",
	"damage": 1
}

def blood_attack(p1, p2):
	global fist
	# p1 is the attacker
	weapon = fist
	for item in p1.equiped:
		if item['type'].split('-')[0] == 'weapon':
			weapon = item
			break


	damage = weapon['damage']
	#got damage from weapon now decrease it by armor unless its magic
	
	p1.getHit(damage/2)
	if weapon != fist:
		p1.usedItem(weapon)
	
	damage = damage * 2

	if weapon['type'].split('-')[1] != 'magic':
		damage -= p2.defense
		for item in p2.equiped:
			if item['type'].split('-')[0] == 'shield':
				damage -= item['defense']
			elif item['type'].split('-')[0] == 'armor':
				damage -= item['defense']
	
	if damage < 0:
		damage = 0
		
	p2.getHit(damage)
	if weapon != fist:
		p1.usedItem(weapon)