import time

class Window:

	def __init__(self, width, height) -> None:
		self.width = width
		self.height = height
		self.slowtime = 0.03
		self.screen = []
		self.line_num = 0
		pass
	
	def clear():
		print("\x1B\x5B2J", end="")
		print("\x1B\x5BH", end="")

	def send_txt(self, str_to_draw:str):
		chunks = []
		if str_to_draw.__contains__('\n'):
			temp_chunks = str_to_draw.split('\n')
			for chunk in temp_chunks:
				lines = [chunk.replace('\n','')[i:i+self.width] for i in range(0, len(chunk), self.width)]
				for line in lines:
					chunks.append(line)
		else:
			chunks = [str_to_draw[i:i+self.width] for i in range(0, len(str_to_draw), self.width)]
		for chunk in chunks:
			if chunks == '':
				chunks.remove(chunk)
		self.draw(chunks)

	def clear(self):
		print("\x1B\x5B2J", end="")
		print("\x1B\x5BH", end="")
	
	def draw(self, chunks):
		#print(chunks)
		input()
		self.clear()
		for chunk in chunks:
			self.screen.append(chunk)
		index = 0
		hook_index = 0
		while True:
			try:
				self.screen[index]
			except:
				break
			if 'hook' in self.screen[index]:
				self.screen[index] = self.screen[index].replace('hook','')
				hook_index = index
			print(self.screen[index])
			index += 1
			time.sleep(self.slowtime)
			if index == self.height:
				input()
				self.clear()
				delete = hook_index if hook_index != 0 else self.height
				try:
					self.screen = self.screen[delete:]
					index = 0
				except:
					index = 0
					break
				

		
