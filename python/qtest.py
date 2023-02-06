import json
one_part = '"add_text_1": ["&0","txt1.txt"],'
if one_part[-1] == ',':
	one_part = one_part[:-1]
try:
	parsed_json = json.loads('{'+one_part+'}')
	print('Went well!')
except ValueError as err:
	print(err)