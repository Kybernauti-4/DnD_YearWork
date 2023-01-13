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
			
			if len(self.fast_render) > 0 and 'hook' in self.fast_render[delete]:
				delete +=1
				while True:
					if 'hook' in self.fast_render[delete]:
						delete += 1
					else:
						break
			
			if len(self.fast_render) > 0 and 'unhook' in self.fast_render[delete]:
				self.screen = self.screen[delete+1:]
				delete = 0
			
			self.clear()
			curr_height = 0
			curr_width = 0
			i = 0

			for fast_line in self.fast_render:
				words = fast_line.split(' ')
				for word in words:
					print(word, end="", flush=True)
					curr_width += len(words[i])
					try:
						if curr_width + len(words[i+1]) > len(fast_line):
							print()
							curr_width = 0
							curr_height += 1
						elif curr_width + len(words[i+1]) > self.width:
							print()
							curr_width = 0
							curr_height += 1
					except:
						i = 0
						break
					print(" ", end="", flush=True)
					curr_width += 1
					
			print()
			print(curr_height)
			input()
			curr_width = 0
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
				if curr_width + len(word) > len(line):
						print()
						curr_width = 0
						curr_height += 1
				elif curr_width + len(word) > self.width:
					print()
					curr_width = 0
					curr_height += 1
				print(" ", end="", flush=True)
				time.sleep(self.slowtime)
				curr_width += 1
			

			if len(self.fast_render) < self.height-1:
				self.fast_render.append(line)
			else:
				del self.fast_render[delete]
				self.fast_render.append(line)
			del self.screen[0]
		
window = window(60, 10)
text = open('test.txt', 'r').read()
window.add_text(text)
window.render()
