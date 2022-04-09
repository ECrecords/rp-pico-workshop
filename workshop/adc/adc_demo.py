from utime import sleep_ms
from machine import PWM, ADC, Pin

MAX_PERIOD_NS = 20E6

MIN_DUTY = 0.02
MAX_DUTY = 0.105

MIN_POT_VALUE = 0.0
MAX_POT_VALUE = 65535.0

MAP_VALUE = MAX_DUTY/MAX_POT_VALUE

servo = PWM(Pin(1))

pot = ADC(Pin(26))

def get_duty(pwm: PWM) -> float:
    global MAX_PERIOD_NS
    return pwm.duty_ns()/MAX_PERIOD_NS  # type: ignore

def set_duty(pwm: PWM, duty: float) -> None:
    global MAX_PERIOD_NS
    pwm.duty_ns(round(duty*MAX_PERIOD_NS))

def map (x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;



servo.freq(50)


while True:
    pot_val = pot.read_u16() 
    mapped_val = map(x= pot_val,in_min=MIN_POT_VALUE, in_max=MAX_POT_VALUE, out_min=MIN_DUTY, out_max=MAX_DUTY)
    set_duty(servo, mapped_val)
    print('Servo Duty Cycle: {:.5f}% = {:.5f}ms'.format((servo.duty_ns()/MAX_PERIOD_NS)*100, servo.duty_ns()/1E6), end='\r')  # type: ignore
    sleep_ms(10)
