import time
#FIXME AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
class qtest():

	def __init__(self, width, height) -> None:
		self.height = height
		self.width = width
		self.slowtime = 0.03
		self.screen = []
		pass
			
	def clear(self):
		print("\x1B\x5B2J", end="")
		print("\x1B\x5BH", end="")

	def format_text(self, text):
		lines = text.splitlines()
		formated_chunks = []
		for line in lines:
			words = line.split(' ')
			print(words)
			formatted_line = []
			line_len = 0
			for word in words:
				line_len += len(word)
				if line_len < self.width:
					formatted_line.append(word)
				else:
					formated_chunks.append(formatted_line)
					formatted_line = []
					line_len = 0
		
		print(formated_chunks) # add spaces
		
window = qtest(10, 10)
text = open('test.txt', 'r').read()
window.format_text(text)