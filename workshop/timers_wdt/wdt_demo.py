from utime import sleep, sleep_ms
from machine import Pin, WDT
import machine

starve = False

def feed_pin_isr(calback_ref):
    global starve
    starve = True
    
starve_pin = Pin(0, Pin.IN, Pin.PULL_UP)
starve_pin.irq(feed_pin_isr, Pin.IRQ_FALLING)

count = 0
print("Beginning of Program")

dog = WDT(timeout=5000)
dog.feed()

print("Dog initally fed")
while True:
    if not starve:
        dog.feed()

    print(count)
    count += 1
    sleep_ms(500)        