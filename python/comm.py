import serial
import serial.tools.list_ports
import json
from time import sleep

#global variables
terminator = "\r\n"
comm = {};
last_send = ''

def findDevices():
	ports = serial.tools.list_ports.comports()
	print(ports[0].name)
	counter = 0
	while counter<len(ports):
		try:
			temp_comm = serial.Serial(ports[counter].name, 112500, timeout=1)
			comm.update({counter:temp_comm})
			if(playerID == 'player'):
				print("Succsesfully added port: " + ports[counter].name)
				comm.update({playerID:counter})
			else:
				print("Wrong device on port: " + ports[counter].name)
				comm.popitem()
			counter += 1
		except Exception as e:
			print("Can't open the port: " + ports[counter].name)
			print(e)
			counter += 1

	fix_count = 0
	key = list(comm.keys)
	val = list(comm.values)
	while fix_count < key.len - 1:
		if()

def sendMessage(index,msg):
	b_msg = bytes(msg + terminator, 'UTF-8')
	global last_send
	last_send = b_msg
	comm[index].write(b_msg)
	
def readMessage(index, decoding = False, encoding = 'UTF-8'):
	data = comm[index].readlines()
	iterator = iter(data)
	index = 0
	while(next(iterator) == last_send):
		index += 1
	
	better_data = data[index:]
	return (better_data[0].decode('UTF-8')).strip() if decoding else better_data[0]

def readMessageBlock(index,decoding = False, encoding = 'UTF-8'):
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

def playerID(comport):
	sendMessage(comport,"ID")
	id_rcvd = readMessage(comport, True)
	if((index_start := id_rcvd.index("[")) > 0 and (index_end := id_rcvd.index("]")) > 0):
		ind_string = str(id_rcvd[index_start+1:index_end])


findDevices()
#while True:
#	message = input()
#	sendMessage(0,message)
#	print(readMessage(0,True))