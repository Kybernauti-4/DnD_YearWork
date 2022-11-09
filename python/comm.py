import serial
import serial.tools.list_ports
from time import sleep

#global variables
terminator = "\r\n"
comm = [];
last_send = ''

def findDevices():
	ports = serial.tools.list_ports.comports()
	print(ports[0].name)
	counter = 0
	while counter<len(ports):
		try:
			temp_comm = serial.Serial(ports[counter].name, 112500, timeout=1)
			comm.append(temp_comm)
			sendMessage(counter,"ID")
			if (readMessage(counter,1)=='Giganto'):
				print("Succsesfully added port: " + ports[counter].name)
			else:
				print("Wrong device on port: " + ports[counter].name)
				comm.pop()
			counter += 1
		except Exception as e:
			print("Can't open the port: " + ports[counter].name)
			print(len(comm))
			print(e)
			counter += 1

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


findDevices()
#while True:
#	message = input()
#	sendMessage(0,message)
#	print(readMessage(0,True))