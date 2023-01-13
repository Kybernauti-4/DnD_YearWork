def print_text(text, window):
	window.add_text(text)
	while True:
		window.format_render()
		window.show()