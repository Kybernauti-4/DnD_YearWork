from machine import Pin
from time import sleep
import json
import os
import rp2

led = Pin(25, Pin.OUT)
led.toggle()
#protection sleep boot time
sleep(2)

led.toggle()

repair_count = 0

while True:
	recv_msg = input()
	if recv_msg == "ID":
		f = open('player.json','r')
		data = json.load(f)
		ID = data["ID"]
		f.close()

		print(ID)
		led.toggle()
	elif recv_msg == "IDError":
		readf = open('player.json','r')
		data = json.load(readf)
		ID = data["ID"]
		startIndex = ID.index("[")
		endIndex = ID.index("]")
		playerID = ID[startIndex+1:endIndex]
		newID =("player[" + playerID.replace(str(repair_count-1),'') + str(repair_count)+"]")
		data["ID"] = newID
		readf.close()
		writef = open('player.json','w')
		json.dump(data, writef)
		writef.close()
		led.toggle()
		repair_count+=1
	elif recv_msg == "RepairID":
		readf = open('player.json','r')
		data = json.load(readf)
		ID = data["ID"]
		startIndex = ID.index("[")
		endIndex = ID.index("]")
		playerID = ID[startIndex+1:endIndex]
		newID =("player[" + playerID.replace(str(repair_count),'') + str(repair_count)+"]")
		data["ID"] = newID
		readf.close()
		writef = open('player.json','w')
		json.dump(data, writef)
		writef.close()
		led.toggle()
		repair_count = 0
	else:
		print (recv_msg + " -ack")
		led.toggle()
	