from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)
led.toggle()

while True:
    recv_msg = input()
    print (recv_msg + " -ack")
    print("Hello from pico!")
    led.toggle()
    