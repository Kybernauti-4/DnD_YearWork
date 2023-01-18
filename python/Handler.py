import stack

class Handler:
	def __init__(self, stack)->None:
		self.stack = stack
		pass

	def handle(self, function, args, tags):
		pass
	
	def append_value(self, id, value):
		self.stack.append([id, value])

	def get_value(self, index):
		return self.stack.getValue(index=index)

	def get_stack(self):
		return self.stack

	def id_builder(self, target_id, tags):
		pass

	def id_parser(self, id):
		fsplit = id.split("_")
		id = fsplit[0]
		tags = fsplit[1]
		tags = tags.replace("<", "")
		tag_array = tags.split(">")
		if tag_array[-1] == "":
			tag_array.pop()
		return id, tag_array

valstack = stack.listStack()
handler = Handler(valstack)
id = '1_<o><i><v>'
#print(handler.id_parser(id))
value = 'test'
handler.append_value(id, value)
print(handler.get_value(0))
valstack=handler.get_stack()
print(valstack.getValue(id='1'))