import os
import sys
import importlib
import_path = os.path.join(os.getcwd(),'story/events_scripts')

sys.path.insert(1,import_path)

event_scripts_list = [event.replace('.py','') for event in os.listdir(import_path) if os.path.isfile(os.path.join(import_path, event))]
import_list = []

for event in event_scripts_list:
	import_list.append(importlib.import_module(event.replace('.py','')))

imports = {keys:values for keys in event_scripts_list for values in import_list}
print(imports)

def handle(event_string, arguments):
	function = getattr(imports[event_string],event_string)
	function(arguments)
	
	