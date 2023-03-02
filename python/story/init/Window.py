from time import sleep
from math import ceil
import threading

class Window():

	def __init__(self, width, height) -> None:
		self.height = height
		self.width = width

		self.slowtime = 0.03
		self.screen = []
		self.render = []
		self.render_amount = 0

		self.start_index = 0
		self.end_index = 0
		self.skip = 0
		self.curr_height = 0
		self.curr_width = 0

		self.return_value = None
		self.return_value_set = False

		self.got_input = threading.Event()
		pass

	def add_text(self, text):
		hook_count = 0
		max_word_len = 0
		max_break_num = 0
		for line in (text.splitlines() if type(text) == str else text):
			if '<h>' in line:
				hook_count += 1
			if '<un>' in line:
				hook_count = 0
			for word in line.split(' '):
				if len(word) > max_word_len:
					max_word_len = len(word)
			if ceil(len(line)/self.width) > max_break_num:
				max_break_num = ceil(len(line)/self.width)
		
		if hook_count >= self.height:
			raise Exception("Too many hooks in text for screen")
		elif max_word_len > self.width:
			raise Exception("Words too long for screen")
		elif max_break_num > self.height:
			raise Exception("Lines too long for screen")
		elif self.height - max_break_num < hook_count:
			raise Exception("Too many hooks in text for screen")

		for line in (text.splitlines() if type(text) == str else text):
			self.screen.append(line)
			self.render_amount += 1

	def clear(self):
		print("\x1B\x5B2J", end="")
		print("\x1B\x5BH", end="")
		pass

	def start_auto_render(self):
		self.ar_thread = threading.Thread(target=self.auto_render)
		self.thread_run = True
		self.ar_thread.start()

	def stop_auto_render(self):
		self.thread_run = False
		self.ar_thread.join()
	
	def auto_render(self):
		while self.thread_run:
			in_val = input()
			if self.render_amount > 0:
				self.format_render()
				self.render_amount -= 1
				
			
				if self.return_value_set:
					if in_val != '':
						self.return_value = in_val
						self.return_value_set = False
						self.got_input.set()
				
				try:
					if('<r>' in self.render[-1]):
						self.return_value_set = True
						for i in range(len(self.screen)):
							if self.render[-1] == self.screen[i]:
								self.screen[i] = self.render[-1].replace('<r>', '')
					else:
						self.return_value_set = False
				except:
					pass

				self.do_render()

			else:
				if self.return_value_set:
					print(f'\u001b[A', end='', flush=True)
					if in_val != '':
						self.return_value = in_val
						self.return_value_set = False
						self.got_input.set()
				else:
					print(f'\u001b[A', end='', flush=True)
					continue
	
	

	def get_return_value(self):
		self.got_input.wait()
		self.got_input.clear()
		r = self.return_value
		self.return_value = None
		return r
		

	def format_render(self):

		try:
			line = self.screen[self.end_index]
		except:
			return

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
		if self.height % line_break_num != 0:
			if self.curr_height + line_break_num >= self.height:
				self.start_index += 1
				self.curr_height -= line_break_num
		else:
			if self.curr_height >= self.height:
				self.start_index += 1
				self.curr_height -= line_break_num

		i = self.skip


		if i != 0 and '<un>' in self.render[i]:
			self.screen[self.screen.index(self.render[self.skip])] = self.render[i].replace('<un>', '')
			self.skip -= 1
			
		if '<h>' in self.render[i]:
			self.screen[self.screen.index(self.render[i])] = self.render[i].replace('<h>', '')
			self.render[i] = self.render[i].replace('<h>', '')
			self.skip += 1
				
				

	def do_render(self):
		fast_render = self.end_index - self.start_index - (1 if self.start_index == 0 else 0)
		self.clear()
		
		#print(True if self.return_value == None else False)
		for line in self.render:
			self.curr_width = 0
			line = line.replace('<h>', '')
			line = line.replace('<un>', '')
			line = line.replace('<r>', '')
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