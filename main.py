from machine import Pin
from time import sleep
import json
import os
import rp2

import fileHandler

led = Pin(25, Pin.OUT)
led.toggle()
#protection sleep boot time
sleep(2)

led.toggle()

repair_count = 0

filename = 'player.json'

def strBetween(string:str, startStr, endStr):
	try:
		return string[string.index(startStr)+1:string.index(endStr)]
	except:
		raise Exception('Substring not found')

while True:
	recv_msg = input()
	if recv_msg == "ID":
		data = fileHandler.read(filename)
		ID = data["ID"]
		print(ID)
		led.toggle()

	elif recv_msg == "IDError":
		data = fileHandler.read(filename)
		ID = data["ID"]
		try:
			playerID = strBetween(ID,'[',']')
			newID = data['ID'].replace(playerID,playerID+str(repair_count))
		except Exception as e:
			print(e)
			newID = ID
		fileHandler.rewriteJSON(filename, 'ID', data['ID'], newID)
		led.toggle()
		repair_count+=1

	elif recv_msg == "RepairID":
		data = fileHandler.read(filename)
		ID = data["ID"]
		try:
			playerID = strBetween(ID,'[',']')
			newID = newID = ID.replace(playerID,playerID.replace(str(repair_count),''))
		except Exception as e:
			print(e)
			newID = ID
		
		fileHandler.rewriteJSON(filename, 'ID', data['ID'], newID)
		led.toggle()
		repair_count = 0
		
	else:
		print (recv_msg + " -ack")
		led.toggle()
	