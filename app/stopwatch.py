#import hardware used in design
from utime import time_ns
import utime
from machine import Timer, Pin, UART

start_pin = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
pause_pin = Pin(3, mode=Pin.IN, pull=Pin.PULL_UP)
reset_pin = Pin(4, mode=Pin.IN, pull=Pin.PULL_UP)
stop_pin  = Pin(5, mode=Pin.IN, pull=Pin.PULL_UP)

timer = Timer()
timer_exists = False

update = False
option = 0
mode = "Idle"
min = 0
sec = 0
hsec = 0

def handler(callback_ref):
    global update
    update = True

def start_handler(callback_ref):
    global option
    option = 1

def pause_handler(callback_ref):
    global option
    option = 2

def reset_handler(callback_ref): 
    global option
    option = 3

def stop_handler(callback_ref):
    global option
    option = 4

def start():
    global timer
    global timer_exists
    global mode

    if not timer_exists:
        timer.init(freq=100, mode=Timer.PERIODIC, callback=handler)
        timer_exists = True
        mode = 'Running'

def pause():
    global timer
    global timer_exists
    global mode

    if timer_exists:
        timer.deinit()
        timer_exists = False
        mode = 'Paused'
    

def reset():
    global min
    global sec
    global hsec
    
    min = 0
    sec = 0
    hsec = 0

def stop():
    global mode

    pause()
    reset()
    mode = 'Stopped & Reset'


start_pin.irq(handler=start_handler, trigger=Pin.IRQ_FALLING)
pause_pin.irq(handler=pause_handler, trigger=Pin.IRQ_FALLING)
reset_pin.irq(handler=reset_handler, trigger=Pin.IRQ_FALLING)
stop_pin.irq(handler=stop_handler, trigger=Pin.IRQ_FALLING)

switch = {
    1: start,
    2: pause,
    3: reset,
    4: stop
}

while True:

    if (callable(switch.get(option))):
        switch.get(option)()
        option = 0

    if update:
        hsec += 1

        if hsec == 100:
            sec += 1
            hsec = 0

        if sec == 60:
            min += 1
            sec = 0

        update = False
    
    print('{}: {}:{}:{}'.format(mode, min, sec, hsec), end='\r')
    utime.sleep_ms(5)
        
