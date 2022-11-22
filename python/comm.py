import json
from time import sleep

import serial
import serial.tools.list_ports

#global variables
terminator = "\r\n"
comm = {};
last_send = ''

def playerID(comport):
	sendMessage(comport,"ID")
	id_rcvd = readMessage(comport, True) # send for answer with the id and listen for it
	print(id_rcvd) # just a simple check output
	ind_string = '' # empty string to handle the next block
	if((index_start := id_rcvd.index("[")) > 0 and (index_end := id_rcvd.index("]")) > 0):
		# "simple" check if both of the brackets are present in ID, otherwise the slice function would fail
		ind_string = str(id_rcvd[index_start+1:index_end]) # slicing the string
	return ind_string

def chck_player(comport):
	sendMessage(comport,"ID")
	id_rcvd = readMessage(comport, True) # send for answer with the id and listen for it
	print(id_rcvd) # just a simple check output
	ind_string = '' # empty string to handle the next block
	if((index_start := id_rcvd.index("[")) > 0 and (index_end := id_rcvd.index("]")) > 0):
		# "simple" check if both of the brackets are present in ID, otherwise the slice function would fail
		ind_string = str(id_rcvd[:index_start]) # slicing the part before the ID itself
	return ind_string

def findDevices():
	ports = serial.tools.list_ports.comports() # list of all the ports present on the machine
	print(ports[0].name) # just a control line to see in console if reading comports rigt
	counter = 0 # counter for while function and a tool for assigning the ports to a dict
	while counter<len(ports):
		try:
			temp_comm = serial.Serial(ports[counter].name, 112500, timeout=1)
			# open a serial line so I can communicate with the device, if fails, falls to except
			comm.update({counter:temp_comm}) # update the dict with a numerical key
			player_chck = chck_player(counter) # send a message to get the player ID
			print("Got the id!")
			if(player_chck == 'player'):
				# check if the the ID is really id of player
				print("Succsesfully added port: " + ports[counter].name)
				comm.update({playerID(counter):counter})
				# if nothing errored out, good and add the player id and which numerical index of port it has
			else:
				print("Wrong device on port: " + ports[counter].name)
				comm.popitem()
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
	key = list(comm.keys())
	val = list(comm.values())

	while fix_count < (len(key) - 1):
		if(key[fix_count] == str(val[fix_count+1])):
			# if values in criss cross is equal
			comm[str(key[fix_count+1])] = comm[str(key[fix_count])] # replace the values in criss cross
			comm.pop(str(key[fix_count])) # delete the the useless line
			#update all the variables for next loop
			key = list(comm.keys())
			val = list(comm.values())
			fix_count+=1
		else:
			fix_count+=1
			
	# I wrote it last week and I have no idea what the fuck is going on here anymore
	print(comm) # control print

def sendMessage(index,msg):
	# message has to be formated, thus function to format and send
	b_msg = bytes(msg + terminator, 'UTF-8')
	global last_send
	last_send = b_msg
	comm[index].write(b_msg)
	
def readMessage(index, decoding = False, encoding = 'UTF-8'):
	# message has to be read and decoded, if you want
	# !!!!!!!!!!!!!!!!! THIS FUNCTION WILL READ ONE LINE AFTER THE THE FEEDBACK MESSAGE !!!!!!!!!!!!!!!!!
	data = comm[index].readlines()
	iterator = iter(data)
	index = 0
	while(next(iterator) == last_send):
		index += 1
	# used to get the message out of it and not the feedback
	better_data = data[index:]
	return (better_data[0].decode('UTF-8')).strip() if decoding else better_data[0] # return decoded or encoded, doesn't matter

def readMessageBlock(index,decoding = False, encoding = 'UTF-8'):
	# The same as readMessage but used to get the entire block of data coming through
	data = comm[index].readlines()
	iterator = iter(data)
	index = 0
	while(next(iterator) == last_send):
		index += 1
	
	better_data = data[index:]
	if decoding:
		counter = 0
		for line in better_data:
			better_data[counter] = (line.decode(encoding)).strip()
			counter += 1
	
	return better_data




findDevices()
#while True:
#	message = input()
#	sendMessage(0,message)
#	print(readMessage(0,True))