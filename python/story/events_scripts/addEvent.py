import json
import os

def addEvent(path, event_name, args):
	with open(os.path.join(path, 'events.json'), 'r') as file:
		events_args = json.load(file)
	
	events = list(events_args.keys())
	events_num:dict = {}
	for event in events:
		eventName = '_'.join(event.split('_')[:-1])
		if eventName not in list(events_num.keys()):
			events_num[eventName] = 1
		else:
			events_num[eventName] += 1
	
	event_num = 1
	if event_name in list(events_num.keys()):
		event_num = events_num[event_name] + 1
	
	events_args[f'{event_name}_{event_num}'] = args

	with open(os.path.join(path, 'events.json'), 'w') as file:
		json.dump(events_args, file, indent=4)
	

if __name__ == '__main__':
	addEvent('story\\Chapter_1\\Encounter_1\\Scene_2', 'test', ['test'])