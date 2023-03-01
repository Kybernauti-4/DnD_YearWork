import serial.tools.list_ports

import comm

devices = {}


def playerID(comport):
	comm.sendMessage(comport,"ID")
	return comm.readMessage(comport, True)

def chck_player(comport):
	comm.sendMessage(comport,"type")
	if comm.readMessage(comport, True) == "player":
		return True
	else:
		return False

def id_fix(comport): # can be run just as a check
	while playerID(comport-1) == playerID(comport): 
		comm.sendMessage(comport, "IDError")
	

def findDevices():
	ports = serial.tools.list_ports.comports() # list of all the ports present on the machine
	counter = 0 # counter for while function and a tool for assigning the ports to a dict
	while counter<len(ports):
		try:
			temp_device = serial.Serial(ports[counter].name, 112500, timeout=1)
			# open a serial line so I can communicate with the device, if fails, falls to except
			devices.update({counter:temp_device}) # update the dict with a numerical key
			#print('Opened the port: ' + ports[counter].name) # just a control line to see in console if reading comports rigt
			if chck_player(devices[counter]): # check if the device is a player
				# check if the the ID is really id of player
				if counter > 0:
					id_fix(devices[counter])
				devices.update({playerID(devices[counter]):counter})
				#print("Succsesfully added port: " + ports[counter].name)			# if nothing errored out, good and add the player id and which numerical index of port it has
			else:
				#print("Wrong device on port: " + ports[counter].name)
				devices.popitem()
				# wrong id came through and player isn't on the other side and delete the comport from the list
			counter += 1
			# everything went well so we can move on to the next comport
		except Exception as e:
			#print("Can't open the port: " + ports[counter].name)
			print(e)
			counter += 1
			# something errored out, print it and continue on the next port

	# the dict has a fucky wucky structure so fix it
	fix_count = 0
	key = list(devices.keys())
	val = list(devices.values())
	
	while fix_count < (len(key) - 1):
		if(str(key[fix_count]) == str(val[fix_count+1])):
			#print("Fixing the dictionary!")
			# if values in criss cross is equal
			devices[key[fix_count+1]] = devices[key[fix_count]] # replace the values in criss cross
			devices.pop(key[fix_count]) # delete the the useless line
			#update all the variables for next loop
			key = list(devices.keys())
			val = list(devices.values())
			fix_count+=1
		else:
			fix_count+=1
	#print(devices)	
	# I wrote it last week and I have no idea what the fuck is going on here anymore
	return devices

if __name__ == "__main__":
	print(findDevices())