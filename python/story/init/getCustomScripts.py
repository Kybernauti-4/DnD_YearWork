import comm
import deviceHandler

def getCustomScripts():
	try:
		devicesDict = deviceHandler.findDevices()
	except: devicesDict = {}

	for id,device in devicesDict.items():
		comm.sendMessage(device, 'scripts_list')
		scripts_list = comm.readMessage(device, True)
		print(scripts_list[0])
		print(type(scripts_list))

if __name__ == '__main__':
	getCustomScripts()