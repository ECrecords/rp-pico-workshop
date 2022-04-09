# Author: Elvis Chino-Islas
# Date: 4/9/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the GPIO on the
#   RP-RP2 along with demoing interrupts

from machine import Pin
from utime import sleep_ms

## Interrupt Service Routine
def pin1_irq_handler(pin: Pin):
    global irq_trigged
    irq_trigged = True

# Used to keep track if interrupt occurred
irq_trigged = False

# Initializes the GP0 to be an input while being pulled down
pin0 = Pin(0, mode=Pin.IN, pull=Pin.PULL_DOWN)

# Initializes the GP1 to be an input while being pulled up
pin1 = Pin(1, mode=Pin.IN, pull=Pin.PULL_UP)

# Initializes the GP25 (on-board led) while being pulled down
led = Pin(25, mode=Pin.OUT, pull=Pin.PULL_DOWN)

# Enables an interrupt on GP1 that is triggered on a falling edge
## uses a hardware interrupt
pin1.irq(handler=pin1_irq_handler, trigger=Pin.IRQ_FALLING, hard=True)

# Declares and initializes the count to 0
count = 0

#TODO add a new GPIO pin that can break this loop
while True:

    # blinks led on and off
    led.toggle()

    # Checks if the interrupt was recently triggered
    if irq_trigged:
        print("interrupt detected @ GP1, count reset")
        # Resets count
        count = 0
        # Marks most recent interrupt was handeled
        irq_trigged = False
    else:
        # Reads value of GP0 and if it is high it will
        # increment the counter
        if pin0.value():
            count += 1

    print(count, end='\r')

    # CPU waits for 10 ms till next iteration
    sleep_ms(10)
    
print("Program Ended")

    
