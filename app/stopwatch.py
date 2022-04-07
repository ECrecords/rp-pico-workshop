#import hardware used in design
import machine
from machine import Timer, Pin, UART

start = Pin(3, mode=Pin.IN, pull=Pin.PULL_UP)
pause = Pin(4, mode=Pin.IN, pull=Pin.PULL_UP)
reset = Pin(5, mode=Pin.IN, pull=Pin.PULL_UP)
stop  = Pin(6, mode=Pin.IN, pull=Pin.PULL_UP)

timer = Timer()
timer_exists = False

update = False

mode = None
min = 0
sec = 0
hsec = 0

def handler(callback_ref):
    global update
    update = True

def start_handler(callback_ref):
    start_trigger = True;

def pause_handler(callback_ref):
    pause_trigger = True;

def reset_handler(callback_ref): 
    reset_trigger = True;

def stop_handler(callback_ref):
    stop_trigger = True;
    


start.irq(handler=start_handler, trigger=Pin.IRQ_FALLING)
pause.irq(handler=pause_handler, trigger=Pin.IRQ_FALLING)
reset.irq(handler=reset_handler, trigger=Pin.IRQ_FALLING)
stop.irq(handler=stop_handler, trigger=Pin.IRQ_FALLING)


timer.init(freq=100, mode=Timer.PERIODIC, callback=handler)

while True:



    if update:
        hsec += 1

        if hsec == 100:
            sec += 1
            hsec = 0

        if sec == 60:
            min += 1
            sec = 0

        update = False
    
    print('{}:{}:{}'.format(min, sec, hsec), end='\r')
        
