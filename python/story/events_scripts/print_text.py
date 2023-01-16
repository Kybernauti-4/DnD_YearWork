def print_text(text, window, autorender=False):
	if type(text) == str:
		window.add_text(text)
	elif type(text) == list:
		for line in text:
			window.add_text(line)
	if not autorender:
		window.format_render()
		window.show()