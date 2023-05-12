def combatState(enemyList):
	for key,enemy in enemyList.items():
		if enemy.info['status'] == 'alive':
			return 'combat'
		else:
			return 'victory'