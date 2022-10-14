import json

import serial
from time import sleep

#global variables
terminator = "\r\n"

comm = serial.Serial('COM3', 112500, timeout=0.01)
comm.flush()
last_send = ''


# This is the first general file
class player:

	def __init__(self, PlayerData):
		self.HP = PlayerData['HP']
		self.MP = PlayerData['MP']
		self.Name = PlayerData['Name']
		self.Age = PlayerData['Age']
		self.Gender = PlayerData['Gender']


# working file code, reuse later, commented for now

#f = open('player.json',)

#player_data = json.load(f)
#Giganto = player(player_data["player info"][0])

# f.close()

# print(Giganto.HP)

#def all_equal(iterator):
#	iterator = iter(iterator)
#	try:
#		first = next(iterator)
#	except StopIteration:
#		return True
#	return all(first == x for x in iterator)

def sendMessage(msg):
	b_msg = bytes(msg + terminator, 'UTF-8')
	global last_send
	last_send = b_msg
	comm.write(b_msg)


def readMessage(decoding = False, encoding = 'UTF-8'):
	data = comm.readlines()
	if (last_send == data[0]):
		better_data = data[not_include:len(data)]
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


while True:
	message = input()
	sendMessage(message)
	print(readMessage(True))