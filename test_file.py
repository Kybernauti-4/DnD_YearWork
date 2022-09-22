import json
import yaml
from yaml.loader import SafeLoader

#This is the first general file
class player:
    
    def __init__(self, PlayerData):
        self.HP = PlayerData['HP']
        self.MP = PlayerData['MP']
        self.Name = PlayerData['Name']
        self.Age = PlayerData['Age']
        self.Gender = PlayerData['Gender']

f = open('player.json',)

player_data = json.load(f)
Giganto = player(player_data["player info"][0])

f.close()


print(Giganto.HP)

player_file = open("player.yml", "r")
player_yaml_data = yaml.load(player_file, Loader=SafeLoader)

Magnifico = player(player_yaml_data['player_info'])

print(Magnifico.HP)