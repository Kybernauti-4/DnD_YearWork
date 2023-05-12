import json
import os

def addEvent(path,event_index, event_name, args):
	if type(event_name) == str:
		with open(os.path.join(path, 'events.json'), 'r') as file:
			events_args = json.load(file)
		
		events = list(events_args.keys())
		args_split = list(events_args.values())
		i=0
		event_num = 1
		for event in events:
			if i>event_index:
				break

			if event_name == '_'.join(event.split('_')[:-1]):
				event_num += 1

			i += 1
		
		event_name += f"_{event_num}"
		#events_args[f'{event_name}_{event_num}'] = args
		events.insert(event_index+1,event_name)

		for i in range(len(events)):
			if events[i] in events[i+1:]:
				index_of_copy = events[i+1:].index(events[i])
				event_wo_num = '_'.join(events[i].split('_')[:-1])
				num = int(events[i].split('_')[-1])+1
				events[i+1+index_of_copy] = f'{event_wo_num}_{num}'

		args_split.insert(event_index+1,args)

		events_args = {events[i]:args_split[i] for i in range(len(events))}
		with open(os.path.join(path, 'events.json'), 'w') as file:
			json.dump(events_args, file, indent=4)
		

	elif type(event_name) == list:
		i = 0
		for event in event_name:
			addEvent(path, event_index+i, event, args[i])
			i += 1
	
	else:
		raise TypeError('event_name must be either a string or a list of strings')
	

