from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

while True:
    led.toggle()
    receive_data = input()
    return_data = receive_data;
    print(return_data+' acknowledged')
    print(b"This is a message from pico W")