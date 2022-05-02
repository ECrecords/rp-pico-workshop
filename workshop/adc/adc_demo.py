# Author: Elvis Chino-Islas
# Date: 4/9/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the PWM and ADC on the
#   RP-RP2 to control a servo

from utime import sleep_ms
from machine import PWM, ADC, Pin
from micropython import const

# The maximum period (50Hz) in nanoseconds
MAX_PERIOD_NS = 20E6

# Minimum Duty Cycle
MIN_DUTY = 0.02
# Maximum Duty Cycle
MAX_DUTY = 0.105

# Minimum Value for ADC
MIN_POT_VALUE = 0.0

# Maximum Value for ADC
## ADC takes samples 0V - 3.3V using 16 bits
## therefore 2^16 -1 is the maximum value
MAX_POT_VALUE = 65535.0

# General function used to calculate the
# current duty cycle on a PWM object
def get_duty(pwm: PWM) -> float:
    global MAX_PERIOD_NS
    return pwm.duty_ns()/MAX_PERIOD_NS  # type: ignore

# General function used to set the
# duty cycle on a PWM object. 
def set_duty(pwm: PWM, duty: float) -> None:
    global MAX_PERIOD_NS
    pwm.duty_ns(round(duty*MAX_PERIOD_NS))

# Used to map a single value n in domain in to some domain out
## is sued to map ADC range to duty cycle range
def map (x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

# Main
if __name__ == '__main__':
    # Declare and initialize a PWM object @ GP1
    servo = PWM(Pin(1))
    # Sets PWM frequency to 50 Hz
    servo.freq(50)

    # Declare and initializes GP26 as a ADC (ADC0)
    pot = ADC(Pin(26))

    while True:
        # Samples GP26 (ADC0)
        pot_val = pot.read_u16() 

        # Mappes sampled value to duty cycle range
        mapped_val = map(x= pot_val,in_min=MIN_POT_VALUE, in_max=MAX_POT_VALUE, out_min=MIN_DUTY, out_max=MAX_DUTY)

        # set the PWM duty cycle
        set_duty(servo, mapped_val)

        # calculates pulse width (ms)
        pulse_width_ms = servo.duty_ns()/1E6 # type: ignore
        # calculates duty cycle (%)
        duty_cycle_per = (servo.duty_ns()/MAX_PERIOD_NS)*100 # type: ignore

        #Prints the current duty cycle (%) and pulse width (ms)
        print('Servo Duty Cycle: {:2.3f}% = {:.3f}ms'.format(duty_cycle_per, pulse_width_ms), end='\r')  # type:
        
        # CPU waits for 10 ms till next iteration
        ## this allows the servo to get into position
        sleep_ms(10)
