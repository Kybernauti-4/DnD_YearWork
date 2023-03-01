from machine import Pin
from time import sleep

import json
import os

import fileHandler
	
led = Pin(25, Pin.OUT)
led.toggle()
#protection sleep boot time
sleep(2)

led.toggle()
filename = ''
for file in os.listdir():
	if file.endswith(".json"):
		filename = file

		
try:
	repair_count = int(fileHandler.readJSON(filename, 'RPC')) if (fileHandler.readJSON(filename, 'RPC') != 'NoFileError') else 0
except:
	repair_count = 0
	pass

def strBetween(string:str, startStr, endStr):
	try:
		return string[string.index(startStr)+1:string.index(endStr)]
	except:
		raise Exception('Substring not found')

def compareCaseIns(*string:str):
	iterator = iter(string)
	try:
		first = next(iterator)
	except StopIteration:
		return True
	return all(first.lower() == x.lower() for x in iterator)

def clear():
    print("\x1B\x5B2J", end="")
    print("\x1B\x5BH", end="")

while True:
	recv_msg = input()
	led.toggle()
	if compareCaseIns(recv_msg, 'ID'):
		data = fileHandler.read(filename)
		ID = data["ID"]
		print(ID)
		led.toggle()

	elif compareCaseIns(recv_msg, 'type'):
		data = fileHandler.read(filename)
		type = data["type"]
		print(type)
		led.toggle()

	elif compareCaseIns(recv_msg, 'IDError'):
		data = fileHandler.read(filename)
		ID = data["ID"]
		try:
			playerID = strBetween(ID,'[',']')
			newID = data['ID'].replace(playerID,playerID.replace(str(repair_count-1),'')+str(repair_count))
		except Exception as e:
			print(e)
			newID = ID
		fileHandler.rewriteJSON(filename, 'ID', data['ID'], newID)
		fileHandler.rewriteJSON(filename, 'RPC', str(repair_count),str(repair_count+1))
		repair_count+=1
		print('ID Moved Up')
		led.toggle()

	elif compareCaseIns(recv_msg, 'IDRepair'):
		data = fileHandler.read(filename)
		ID = data["ID"]
		try:
			playerID = strBetween(ID,'[',']')
			newID = ID.replace(playerID,playerID.replace(str(repair_count-1),''))
		except Exception as e:
			print(e)
			newID = ID
		
		fileHandler.rewriteJSON(filename, 'ID', data['ID'], newID)
		led.toggle()
		repair_count = 0
		print('ID Repaired Up')
		led.toggle()
	
	elif compareCaseIns(recv_msg, 'clear'):
		clear()
		led.toggle()
		
	elif compareCaseIns(recv_msg, 'sendpdata'):
		data = fileHandler.read(filename)
		print(data)
		led.toggle()
	
	elif compareCaseIns(recv_msg, 'scripts_list'):
		print(os.listdir('custom_scripts'))
		led.toggle()
	
	elif compareCaseIns(recv_msg.split('_')[0], 'script'):
		data = fileHandler.read(f'custom_scripts/{recv_msg.split("_")[1]}')
		print(data)
		led.toggle()
		
	else:
		print (recv_msg + " -ack")
		led.toggle()
	