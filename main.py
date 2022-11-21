from machine import Pin
from time import sleep
import json
import os
import rp2

led = Pin(25, Pin.OUT)
led.toggle()

os.mount(rp2.Flash(),'/')

while True:
	recv_msg = input()
	if recv_msg == "ID":
		f = open('player.json')
		data = json.load(f)
		ID = data["ID"]
		f.close()

		print(ID)
		led.toggle()
	else:
		print (recv_msg + " -ack")
		led.toggle()
	