import keyboard

keyboard.on_press(lambda e: print(e.name))

keyboard.wait()