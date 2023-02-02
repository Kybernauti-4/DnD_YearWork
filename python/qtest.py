import keyboard

def function_a(e):
	if e.name == 'a':
		print('You pressed a key!')

def	function_b(e):
	if e.name == 'b':
		print('You pressed b key!')

keyboard.on_press(function_a)
keyboard.on_press(function_b)
keyboard.wait('esc')