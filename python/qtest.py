from time import sleep
import threading
from math import ceil

class window():

	def __init__(self, width, height) -> None:
		self.height = height
		self.width = width
		self.slowtime = 0.03
		self.screen = []
		self.render = []
		self.start_index = 0
		self.end_index = 0
		self.skip = 0
		self.curr_height = 0
		self.curr_width = 0
		pass

	def add_text(self, text):
		for line in text.splitlines():
			self.screen.append(line)

	def clear(self):
		print("\x1B\x5B2J", end="")
		print("\x1B\x5BH", end="")
		pass

	def format_render(self):
		unhook = False

		line = self.screen[self.start_index]
		line_break_num = ceil(len(line)/self.width)
		
		
		if self.curr_height <= self.height:
			self.end_index += 1
		self.curr_height += line_break_num
		
		if self.skip == 0:
			self.render = self.screen[self.start_index:self.end_index]
		else:
			self.render = self.render[:self.skip]
			for line in self.screen[self.start_index+self.skip:self.end_index]:
				self.render.append(line)

		if self.curr_height >= self.height:
			self.start_index += 1
			self.curr_height -= line_break_num

		i = self.skip


		if i != 0 and '<un>' in self.render[i]:
			unhook = True
			self.skip -= 1
			
		while not unhook:
			if '<h>' in self.render[i]:
				self.skip += 1
				i+=1
			else:
				break

	def show(self):
		fast_render = self.end_index - self.start_index - (1 if self.start_index == 0 else 0)
		self.clear()
		for line in self.render:
			self.curr_width = 0
			words = line.split(' ')
			for i in range(len(words)):
				if fast_render> 0: 
					print(words[i], end="", flush=True)
				else:
					for char in words[i]:
						print(char, end="", flush=True)
						sleep(self.slowtime)
				self.curr_width += len(words[i])
				
				try:
					if self.curr_width + len(words[i+1])+1 > self.width:
						print()
						self.curr_width = 0
						continue
				except:
					print()
					continue
				
				print(' ', end="", flush=True)
				self.curr_width += 1
			
			fast_render -= 1
			
				
		
window = window(10, 10)
text = open('test.txt', 'r').read()
window.add_text(text)
while True:
	window.format_render()
	window.show()
	input()
