id = 'global'
name = 'Get Information'

def getInfo(p):
	info_list = []
	for info,num in p.info.items():
		info_list.append(f'{info}: {num}')
	
	return info_list