import serial
import serial.tools.list_ports
from time import sleep

#global variables
terminator = "\r\n"
comm = [];
last_send = ''

def findDevices():
	ports = serial.tools.list_ports.comports()
	counter = 0
	while counter<len(ports):
		try:
			comm.append(serial.Serial(ports[counter], 112500, timeout=1))
			print("Succsesfully added port: " + ports[counter])
			counter += 1
		except:
			print("Can't open the portt: " + ports[counter])
			counter += 1

def sendMessage(msg):
    b_msg = bytes(msg + terminator, 'UTF-8')
    global last_send
    last_send = b_msg
    comm.write(b_msg)
    
def readMessage(decoding = False, encoding = 'UTF-8'):
    data = comm.readlines()
    if(last_send == data[0]):
        better_data = data[1:len(data)]
    else:
        better_data = data
    if decoding:
        counter = 0
        
        for line in better_data:
            better_data[counter] = (line.decode(encoding)).strip()
            counter += 1
        
        return better_data
    else:
        return data

#while True:
    #message = input()
    #sendMessage(message)
    #print(readMessage(True))

findDevices()