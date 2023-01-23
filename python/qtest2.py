import keyboard


def get_input():
	keyboard.on_press(lambda e: print(e))

	keyboard.wait('enter', suppress=True)
	return 'done'

print(get_input())