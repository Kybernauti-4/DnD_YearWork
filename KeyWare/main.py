

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



def read_data():
	global data_left
	global data_right
	global data_left_key
	global data_right_key
	global player_file
	global left_num_led
	global right_num_led
	
	try:
		with open(player_file, 'r') as f:
			data = json.load(f)
	except:
		pass #will fail when the file is being written to

	#data handling
	curr_left = data['info'][data_left_key]
	curr_right = data['info'][data_right_key]
	max_left = data['info']['max_'+data_left_key]
	max_right = data['info']['max_'+data_right_key]

	left_num_led = int(curr_left/max_left*8)
	right_num_led = int(curr_right/max_right*8)

	data_left = [1 if i <= left_num_led else 0 for i in range(8)]
	data_right = [1 if i <= right_num_led else 0 for i in range(8)]





#Data to show
with open('config.json', 'r') as f:
	data = json.load(f)
	data_left_key = data['data_left']
	data_right_key = data['data_right']

player_file = ''
for file in os.listdir():
	if file.endswith('.json'):
		if "player" in file:
			player_file = file
			break
#print("Player file: " + player_file)
		
try:
	repair_count = int(fileHandler.readJSON(player_file, 'RPC')) if (fileHandler.readJSON(player_file, 'RPC') != 'NoFileError') else 0
except:
	repair_count = 0
	pass

read_data()

while True:
	recv_msg = input()
	#blink LED code
	#Everything else
	if compareCaseIns(recv_msg, 'ID'):
		#print(player_file)
		with open(player_file, 'r') as f:
			data = json.load(f)
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
	
	elif compareCaseIns(recv_msg, 'recvFile'):
		file_name = input()
		while True:
			try:
				file = open(file_name, 'w')
				break
			except:
				pass

		data = input()
		file.write(data)
		try:
			json.loads(data)
		except:
			pass #not a json file
		file.close()
		sleep(0.1)
		read_data()

	else:
		print (recv_msg + " -ack")
	