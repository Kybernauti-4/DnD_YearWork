unique_pid = 'global'

def attack(p1, p2, attack_info):
	# p1 is the attacker
	damage = 0
	for item in p1.inventory:
		if item['type'] == 'weapon':
			weapon = item
			break