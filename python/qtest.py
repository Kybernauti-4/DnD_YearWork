import json

json_string = '{"first_name": "Guido"}'
try:
	parsed_json = json.loads(json_string)
	print(parsed_json['first_name'])
except ValueError as err:
	print(err)