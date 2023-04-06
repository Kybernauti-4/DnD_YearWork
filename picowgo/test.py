from machine import Pin, Timer
from time import sleep

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

#boot sequence
bar_len = 20
sleep_len = 0.1
space = " "*bar_len
print(f"[{space}]")
for i in range(bar_len):
    sleep(sleep_len)
    bar = "="*(i+1)
    arrow = ">" if i < bar_len-1 else ""
    space = " "*(bar_len-2-i)
    print(f"\u001b[A[{bar}{arrow}{space}]")

#functions definitions
def turn_ttl_on():
    if not ttl_red.value() and not ttl_blue.value():
        ttl_red.value(1)
    else:
        ttl_red.value(1)
        ttl_blue.value(0)

def turn_ttl_off():
    ttl_blue.value(0)
    ttl_red.value(0)

def switch_ttl():
    if ttl_red.value():
        ttl_red.value(0)
        ttl_blue.value(1)
    else:
        ttl_red.value(1)
        ttl_blue.value(0)

def shift_out(data):
    mr.value(0)
    mr.value(1)

    dsb.value(1)

    for i in range(8):
        dsa.value(data[i-8])
        r_clk.value(1)
        r_clk.value(0)

    sleep(1)
    dsb.value(0)

def add(byte_list):
    carry = 1
    for i in range(8):
        byte_list[7-i] += carry
        carry = byte_list[7-i] // 2
        byte_list[7-i] %= 2
        if carry == 0:
            break
    return byte_list

#main loop/testing
byte_list = [0,0,0,0,0,0,0,0]
def timer_callback(timer):
    global byte_list
    shift_out(byte_list)
    byte_list = add(byte_list)

timer = Timer(mode = Timer.PERIODIC, period = 1, callback = timer_callback)
