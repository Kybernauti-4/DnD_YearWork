import json

import serial
from time import sleep

#global variables
terminator = "\r"


#This is the first general file
class player:
    
    def __init__(self, PlayerData):
        self.HP = PlayerData['HP']
        self.MP = PlayerData['MP']
        self.Name = PlayerData['Name']
        self.Age = PlayerData['Age']
        self.Gender = PlayerData['Gender']


#working file code, reuse later, commented for now

#f = open('player.json',)

#player_data = json.load(f)
#Giganto = player(player_data["player info"][0])

#f.close()

#print(Giganto.HP)

comm = serial.Serial('COM3', 112500, timeout=0.1)

while True:
    send_data = input()
    comm.write(bytes(send_data+terminator, 'UTF-8'))
    sleep(1)
    received_data = comm.readlines()[1]
    print(received_data.decode('UTF-8'))
    new_message = comm.readline()
    print(new_message)
    