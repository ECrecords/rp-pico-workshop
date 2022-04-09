from machine import Pin
from utime import sleep_ms

def pin1_irq_handler(pin: Pin):
    global irq_trigged
    irq_trigged = True


irq_trigged = False

pin0 = Pin(0, mode=Pin.IN, pull=Pin.PULL_DOWN)

pin1 = Pin(1, mode=Pin.IN, pull=Pin.PULL_UP)

pin1.irq(handler=pin1_irq_handler, trigger=Pin.IRQ_FALLING, hard=True)

count = 0

while True:
    if irq_trigged:
        print("interrupt detected @ GP1, count reset")
        count = 0
        irq_trigged = False
    else:
        if pin0.value() == 1:
            count += 1

    print(count, end='\r')
    sleep_ms(10)
    
