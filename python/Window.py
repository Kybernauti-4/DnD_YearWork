import time
import os

class Window:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.time_0 = time.perf_counter_ns()
		self.time_1 = time.perf_counter_ns()
		self.show_bool = False
		self.screen = []
		self.line_num = 0
	
	def clear():
		print("\x1B\x5B2J", end="")
		print("\x1B\x5BH", end="")

	def draw(self, str_to_draw):
		chunks = [str_to_draw[i:i+self.width] for i in range(0, len(str_to_draw), self.width)]
		self.screen.append(chunks)
		if (self.line_num + len(chunks)) < self.height:
			for line in chunks:
				print(line.replace('hook',''))
				self.line_num += 1
		else:
			os.system('cls')
			for i in range(len(self.screen)):
				index = -(i + 1 - len(self.screen))
				if self.screen[index].__contains__('hook'):
					self.screen = self.screen[index:]
					break
			else:
				self.screen = []
				self.screen.append(chunks)
			self.line_num =0
			for line in chunks:
				print(line.replace('hook',''))
				self.line_num += 1