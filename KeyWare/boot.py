# boot.py -- run on boot-up
from machine import Pin
from utime import sleep, ticks_ms

import _thread
import json
import os

import fileHandler

#protection sleep boot time
sleep(2)

#pin setup
dsa = Pin(0, Pin.OUT)
dsb = Pin(18, Pin.OUT)
mr = Pin(2, Pin.OUT)
r_clk = Pin(1, Pin.OUT)
ttl_red = Pin(4, Pin.OUT)
ttl_blue = Pin(3, Pin.OUT)

#initial state
r_clk.value(0)
mr.value(1)
dsb.value(0)
dsa.value(0)
curr_side = 'left'

left_num_led = 6
right_num_led = 3

data_left = [i if i < left_num_led else 0 for i in range(8)]
data_right = [i if i < right_num_led else 0 for i in range(8)]


def turn_ttl_off():
	ttl_blue.value(0)
	ttl_red.value(0)

def shift_out(data):
	dsb.value(1) #enable data

	for i in range(8): #get then data into the register
		dsa.value(data[i-7])
		r_clk.value(1) #rising edge
		r_clk.value(0)

	dsb.value(0) #disable data

now = ticks_ms()
interval = 100
def LED_blink():
	global curr_side
	global data_right
	global data_left
	global ttl_blue
	global ttl_red
	global now
	global duty_now

	while True:
		try:
			if later:=ticks_ms() - now > interval:
				turn_ttl_off()
				now = later
				if curr_side == 'left':
					shift_out(data_right)
					curr_side = 'right'
					ttl_blue.value(1)

				else:
					shift_out(data_left)
					curr_side = 'left'
					ttl_red.value(1)
		except:
			pass

LED_thread = _thread.start_new_thread(LED_blink, ())