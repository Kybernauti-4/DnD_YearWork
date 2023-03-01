import json
from time import sleep

import serial
import serial.tools.list_ports

#global variables
terminator = "\r\n"
last_send = ''

def sendMessage(comport,msg):
	# message has to be formated, thus function to format and send
	b_msg = bytes(msg + terminator, 'UTF-8')
	global last_send
	last_send = b_msg
	comport.write(b_msg)
	
def readMessage(comport, decoding = False, encoding = 'UTF-8'):
	# message has to be read and decoded, if you want
	# ! THIS FUNCTION WILL READ ONE LINE AFTER THE THE FEEDBACK MESSAGE !
	data = comport.readlines()
	#print(data)
	iterator = iter(data)
	index = 0
	while(True):
		index += 1
		if next(iterator) == last_send:
			break
	# used to get the message out of it and not the feedback
	better_data = data[index:]
	#print((better_data[0].decode('UTF-8')).strip() if decoding else better_data[0])
	return (better_data[0].decode('UTF-8')).strip() if decoding else better_data[0] # return decoded or encoded, doesn't matter

def readMessageBlock(comport,decoding = False, encoding = 'UTF-8'):
	# The same as readMessage but used to get the entire block of data coming through
	data = comport.readlines()
	#print(last_send)
	iterator = iter(data)
	index = 0
	while(True):
		index += 1
		if next(iterator) == last_send:
			break
	
	better_data = data[index:]
	if decoding:
		counter = 0
		for line in better_data:
			better_data[counter] = (line.decode(encoding)).strip()
			counter += 1
	
	return better_data