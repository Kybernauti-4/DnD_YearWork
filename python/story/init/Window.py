import time
import os

class Window:

	def __init__(self, width, height) -> None:
		self.width = width
		self.height = height
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
		
		if len(chunks) > self.height:
			print_chunks = [chunks[i:i+self.height] for i in range(0, len(str_to_draw), self.height)]
			for chunks in print_chunks:
				if len(chunks) != 0:
					self.draw(chunks)

		self.draw(chunks)

	def draw(self, chunks):
		input()
		for chunk in chunks:
			self.screen.append(chunk)

		if len(self.screen) > self.height:
			for i in range(len(self.screen)):
				index = -(i + 1 - len(self.screen))
				if self.screen[index].__contains__('hook'):
					self.screen[index] = self.screen[index].replace('hook','')
					self.screen = self.screen[index:]
					break
			else:
				self.screen = []
				for chunk in chunks:
					self.screen.append(chunk)

		os.system('cls')
		for line in self.screen:
			print(line.replace('hook',''))
