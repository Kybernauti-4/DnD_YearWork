from machine import Pin
from utime import sleep, time_ns

import uasyncio as asyncio
import json
import os

import fileHandler

#protection sleep boot time
sleep(2)

#pin setup
dsa = Pin(0, Pin.OUT)
dsb = Pin(18, Pin.OUT)
mr = Pin(2, Pin.OUT)
r_clk = Pin(1, Pin.OUT)
ttl_red = Pin(4, Pin.OUT)
ttl_blue = Pin(3, Pin.OUT)

#initial state
r_clk.value(0)
mr.value(1)
dsb.value(0)
dsa.value(0)
data_left = [1,0,0,0,0,0,0,0]
data_right = [1,0,0,0,0,0,0,0]
curr_side = 'left'

#Data to show
with open('config.json', 'r') as f:
	data = json.load(f)
	data_left_key = data['data_left']
	data_right_key = data['data_right']

player_file = ''
for file in os.listdir():
	if file.endswith('.json'):
		with open(file, 'r') as f:
			contents = json.load(f)
			try:
				if contents['type'] == 'player':
					player_file = file
			except:
				pass
		break

		
try:
	repair_count = int(fileHandler.readJSON(player_file, 'RPC')) if (fileHandler.readJSON(player_file, 'RPC') != 'NoFileError') else 0
except:
	repair_count = 0
	pass

def turn_ttl_off():
	ttl_blue.value(0)
	ttl_red.value(0)

def shift_out(data):
	dsb.value(1) #enable data

	for i in range(8): #get then data into the register
		dsa.value(data[i-8])
		r_clk.value(1) #rising edge
		r_clk.value(0)

	dsb.value(0) #disable data

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


async def get_input():
	return input()

loop = asyncio.get_event_loop()
input_task = loop.create_task(get_input)
recv_msg = ''
now = time_ns()
while True:
	if input_task.done():
		recv_msg = input_task.result()
		input_task = loop.create_task(get_input)
		clear()
	#blink LED code
	if recv_msg == '':
		if later:=time_ns() - now > 500000:
			turn_ttl_off()
			now = later
			if curr_side == 'left':
				shift_out(data_left)
				curr_side = 'right'
				ttl_blue.value(1)
			else:
				shift_out(data_right)
				curr_side = 'left'
				ttl_red.value(1)


	#Everything else
	elif compareCaseIns(recv_msg, 'ID'):
		data = fileHandler.read(player_file)
		ID = data["ID"]
		print(ID)


	elif compareCaseIns(recv_msg, 'type'):
		data = fileHandler.read(player_file)
		type = data["type"]
		print(type)


	elif compareCaseIns(recv_msg, 'IDError'):
		data = fileHandler.read(player_file)
		ID = data["ID"]
		try:
			playerID = strBetween(ID,'[',']')
			newID = data['ID'].replace(playerID,playerID.replace(str(repair_count-1),'')+str(repair_count))
		except Exception as e:
			print(e)
			newID = ID
		fileHandler.rewriteJSON(player_file, 'ID', data['ID'], newID)
		fileHandler.rewriteJSON(player_file, 'RPC', str(repair_count),str(repair_count+1))
		repair_count+=1
		print('ID Moved Up')


	elif compareCaseIns(recv_msg, 'IDRepair'):
		data = fileHandler.read(player_file)
		ID = data["ID"]
		try:
			playerID = strBetween(ID,'[',']')
			newID = ID.replace(playerID,playerID.replace(str(repair_count-1),''))
		except Exception as e:
			print(e)
			newID = ID
		
		fileHandler.rewriteJSON(player_file, 'ID', data['ID'], newID)

		repair_count = 0
		print('ID Repaired Up')

	
	elif compareCaseIns(recv_msg, 'clear'):
		clear()

		
	elif compareCaseIns(recv_msg, 'sendpdata'):
		data = fileHandler.read(player_file)
		print(data)

	
	elif compareCaseIns(recv_msg, 'scripts_list'):
		print(os.listdir('custom_scripts'))

	
	elif compareCaseIns(recv_msg.split('_')[0], 'script'):
		script_name = '_'.join(recv_msg.split("_")[1:])
		data = fileHandler.read(f'custom_scripts/{script_name}')
		print(data)


	else:
		print (recv_msg + " -ack")

	