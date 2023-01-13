import time
import threading

class window():

	def __init__(self, width, height) -> None:
		self.height = height
		self.width = width
		self.slowtime = 0.03
		self.screen = []
		self.fast_render = []
		pass

	def add_text(self, text):
		for line in text.splitlines():
			self.screen.append(line)

	def clear(self):
		print("\x1B\x5B2J", end="")
		print("\x1B\x5BH", end="")
		pass

	def render(self):
		curr_width = 0
		curr_height = 0
		delete = 0
		while True:
			try:
				line = self.screen[0]
			except IndexError:
				break

			if 'hook' in line:
				delete +=1
				while True:
					if 'hook' in self.screen[delete]:
						delete += 1
					else:
						break
			
			if 'unhook' in line:
				self.screen = self.screen[delete+1:]
				delete = 0
			
			self.clear()
			i = 0
			for fast_line in self.fast_render:
				i += 1
				words = fast_line.split()
				print(words[i], end="", flush=True)
				curr_width += len(words[i])
				try:
					len(words[i+1])
				except:
					break
				if curr_width + len(words[i+1]) > self.width:
					print()
					curr_width = 0
					curr_height += 1

			for word in line.split():
				if curr_height >= self.height:
					input()
					print("\x1B\x5B2J", end="")
					print("\x1B\x5BH", end="")
					curr_height = 0
				for letter in word:
					print(letter, end="", flush=True)
					time.sleep(self.slowtime)

				curr_width += len(word)
				if curr_width + len(word) > self.width:
					print()
					curr_width = 0
					curr_height += 1
				print(" ", end="", flush=True)
				time.sleep(self.slowtime)
				curr_width += 1
			

			if len(self.fast_render) < self.height-1:
				self.fast_render.append(line)
				print(self.fast_render)
				input()
			else:
				del self.fast_render[delete]
				self.fast_render.append(line)
			del self.screen[0]
		
window = window(60, 10)
text = open('test.txt', 'r').read()
window.add_text(text)
window.render()
