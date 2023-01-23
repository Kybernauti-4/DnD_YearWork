def auto_render(window, auto_render = False):
	if not auto_render:
		window.start_auto_render()
		return True
	else:
		window.stop_auto_render()
		return False
	