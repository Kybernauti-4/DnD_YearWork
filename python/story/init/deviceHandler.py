import serial.tools.list_ports

import story.init.comm as comm

devices = {}


def playerID(comport):
	comm.sendMessage(comport,"ID")
	id_rcvd = comm.readMessage(comport, True) # send for answer with the id and listen for it
	ind_string = '' # empty string to handle the next block
	if((index_start := id_rcvd.index("[")) > 0 and (index_end := id_rcvd.index("]")) > 0):
		# "simple" check if both of the brackets are present in ID, otherwise the slice function would fail
		ind_string = str(id_rcvd[index_start+1:index_end]) # slicing the string
	return ind_string

def chck_player(comport):
	comm.sendMessage(comport,"ID")
	id_rcvd = comm.readMessage(comport, True) # send for answer with the id and listen for it
	ind_string = '' # empty string to handle the next block
	if((index_start := id_rcvd.index("[")) > 0 and (id_rcvd.index("]")) > 0):
		# "simple" check if both of the brackets are present in ID, otherwise the slice function would fail
		ind_string = str(id_rcvd[:index_start]) # slicing the part before the ID itself
	return ind_string

def id_chck(comport):
	msg_txt = "IDError"
	while playerID(comport-1) == playerID(comport): 
		comm.sendMessage(comport, msg_txt)
	

def deviceHandler():
	ports = serial.tools.list_ports.comports() # list of all the ports present on the machine
	counter = 0 # counter for while function and a tool for assigning the ports to a dict
	while counter<len(ports):
		try:
			temp_device = serial.Serial(ports[counter].name, 112500, timeout=1)
			# open a serial line so I can communicate with the device, if fails, falls to except
			devices.update({counter:temp_device}) # update the dict with a numerical key
			print('Opened the port: ' + ports[counter].name) # just a control line to see in console if reading comports rigt
			player_chck = chck_player(devices[counter]) # send a message to get the player ID
			if(player_chck == 'player'):
				# check if the the ID is really id of player
				if counter > 0 :
					id_chck(devices[counter])
				devices.update({playerID(counter):counter})
				print("Succsesfully added port: " + ports[counter].name)			# if nothing errored out, good and add the player id and which numerical index of port it has
			else:
				print("Wrong device on port: " + ports[counter].name)
				devices.popitem()
				# wrong id came through and player isn't on the other side and delete the comport from the list
			counter += 1
			# everything went well so we can move on to the next comport
		except Exception as e:
			print("Can't open the port: " + ports[counter].name)
			print(e)
			counter += 1
			# something errored out, print it and continue on the nesxt port

	# the dict has a fucky wucky structure so fix it
	fix_count = 0
	key = list(devices.keys())
	val = list(devices.values())
	
	while fix_count < (len(key) - 1):
		if(str(key[fix_count]) == str(val[fix_count+1])):
			print("Fixing the dictionary!")
			# if values in criss cross is equal
			devices[key[fix_count+1]] = devices[key[fix_count]] # replace the values in criss cross
			devices.pop(key[fix_count]) # delete the the useless line
			#update all the variables for next loop
			key = list(devices.keys())
			val = list(devices.values())
			fix_count+=1
		else:
			fix_count+=1
	print(devices)
	return devices
	# I wrote it last week and I have no idea what the fuck is going on here anymore
	#print(comm) # control print