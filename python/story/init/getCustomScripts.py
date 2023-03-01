import comm
import deviceHandler
import json

def getCustomScripts():
	try:
		devicesDict = deviceHandler.findDevices()
	except: devicesDict = {}

	for id,device in devicesDict.items():
		comm.sendMessage(device, 'scripts_list')
		scripts_list = json.loads(comm.readMessage(device, True).replace("'", '"'))
		#print(scripts_list)
		for script_name in scripts_list:
			comm.sendMessage(device, f'script_{script_name}')
			script = comm.readMessageBlock(device)
			with open(f'story\\player_scripts\\{script_name}.py', 'a') as f:
				for line in script:
					#print(line)
					f.write(line.decode('utf-8').replace("\r\n", ''))
		print(type(scripts_list))

if __name__ == '__main__':
	getCustomScripts()