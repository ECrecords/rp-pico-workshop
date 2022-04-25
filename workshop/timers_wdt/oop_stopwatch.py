import machine
from machine import Pin, Timer, UART
import utime

class Stopwatch:

    def __init__(self, start_pin, pause_pin, reset_pin, stop_pin) -> None:
        irq_status = machine.disable_irq()

        self.start_pin = Pin(start_pin, mode=Pin.IN, pull=Pin.PULL_UP)
        self.pause_pin = Pin(pause_pin, mode=Pin.IN, pull=Pin.PULL_UP)
        self.reset_pin = Pin(reset_pin, mode=Pin.IN, pull=Pin.PULL_UP)
        self.stop_pin = Pin(stop_pin, mode=Pin.IN, pull=Pin.PULL_UP)

        self.tim = Timer()
        self.tim_exists = False

        self.mode = "Idle"
        
        self.min = 0
        self.sec = 0
        self.hsec = 0

        self.start_pin.irq(handler=self.__start_handler, trigger=Pin.IRQ_FALLING)
        self.pause_pin.irq(handler=self.__pause_handler, trigger=Pin.IRQ_FALLING)
        self.reset_pin.irq(handler=self.__reset_handler, trigger=Pin.IRQ_FALLING)
        self.stop_pin.irq(handler=self.__stop_handler, trigger=Pin.IRQ_FALLING)

        machine.enable_irq(irq_status)

    ########## Interrupt Handlers ##########
    def __tick_handler(self, callback_ref):
        self.hsec+= 1

        if self.hsec == 100:
            self.sec += 1
            self.hsec = 0
        
        if self.sec == 60:
            self.min += 1
            self.sec = 0

    def __start_handler(self, callback_ref):
        self.start()

    def __pause_handler(self, callback_ref):
        self.pause()

    def __reset_handler(self, callback_ref):
        self.reset()

    def __stop_handler(self, callback_ref):
        self.stop()

    ########################################
    def __enable(self):
        if not self.tim_exists:
            self.tim.init(freq=100, mode=Timer.PERIODIC, callback=self.__tick_handler)
            self.tim_exists = True

    def __disable(self):
        if self.tim_exists:
            self.tim.deinit()
            self.tim_exists = False

    def start(self):
        self.mode = "Running"
        self.__enable()

    def pause(self):
        self.mode = "Paused"
        self.__disable()

    def reset(self):
        self.min = 0
        self.sec = 0
        self.hsec = 0
    
    def stop(self):
        self.reset()
        self.__disable()


sw = Stopwatch(2,3,4,5)

while True:
    print('{}: {}:{}:{}'.format(sw.mode, sw.min, sw.sec, sw.hsec), end='\r')
    utime.sleep_ms(5)