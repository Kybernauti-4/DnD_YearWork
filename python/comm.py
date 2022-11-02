import serial
import serial.tools.list_ports
from time import sleep

#global variables
terminator = "\r\n"
comm = [];
last_send = ''

def findDevices():
	ports = serial.tools.list_ports.comports()
	print(type(ports[0].name))
	print(ports[0].name)
	print (len(ports))
	counter = 0
	while counter<len(ports):
		try:
			temp_comm = serial.Serial(ports[counter].name, 112500, timeout=1)
			sendMessage("ID")
			sleep(0.1)
			try:
				if (readMessage(1) == 'Giganto'):
					comm.append(temp_comm)
					print("Succsesfully added port: " + ports[counter].name)
			except:
				print("Wrong device on port: " + ports[counter].name)			
			counter += 1
		except:
			print("Can't open the port: " + ports[counter].name)
			counter += 1

def sendMessage(msg):
	b_msg = bytes(msg + terminator, 'UTF-8')
	global last_send
	last_send = b_msg
	comm.write(b_msg)
	
def readMessage(decoding = False, encoding = 'UTF-8'):
	data = comm.readlines()
	iterator = iter(data)
	index = 0
	while(next(iterator) == last_send):
		index += 1
	
	better_data = data[index:]
	return better_data[0].decode('UTF-8') if decoding else better_data[0]

def readMessageBlock(decoding = False, encoding = 'UTF-8'):
	data = comm.readlines()
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

#while True:
	#message = input()
	#sendMessage(message)
	#print(readMessage(True))

findDevices()