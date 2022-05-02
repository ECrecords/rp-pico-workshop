# Author: Elvis Chino-Islas
# Date: 4/9/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the PWM on the
#   RP-RP2 along with controlling a servo

from utime import sleep_ms
from machine import PWM, Pin
from micropython import const

# The maximum period (50Hz) in nanoseconds
MAX_PERIOD_NS = 20E6

# General function used to calculate the
# current duty cycle on a PWM object
def get_duty(pwm: PWM) -> float:
    global MAX_PERIOD_NS

    # Pulse Width / Period = Duty Cycle
    return pwm.duty_ns()/MAX_PERIOD_NS  # type: ignore

# General function used to set the
# duty cycle on a PWM object. 
def set_duty(pwm: PWM, duty: float) -> None:
    ''' Takes in a initalized PWM object and a float (duty) in range (0.0 - 1)'''
    global MAX_PERIOD_NS

    # Duty Cycle * Period = Pulse Width
    pwm.duty_ns(round(duty*MAX_PERIOD_NS))

# Main
if __name__ == '__main__':

    # Declare and initialize GP0 as input and pull it down
    turn = Pin(0, mode=Pin.IN, pull=Pin.PULL_DOWN)

    # Declare and initialize a PWM object @ GP1
    servo = PWM(Pin(1))
    # Sets PWM frequency to 50 Hz
    servo.freq(50)
    
    # Set the current duty cycle to 5%
    cur_duty = 0.05
    # Increment 0.001%
    ## this insures a clean transition
    incr = 0.0001

    while True:

        ## if turn is set to high
        if turn.value():
            #increments the duty cycle by incr
            cur_duty = cur_duty + incr

            # set the PWM duty cycle
            set_duty(servo, cur_duty)
            
        # if duty cycle is greater of equal to 1
        if get_duty(servo) >= 0.1:

            # reset duty cycle to 5%
            cur_duty = 0.05

            # set the PWM duty cycle
            set_duty(servo, 0)

        # calculates pulse width (ms)
        pulse_width_ms = servo.duty_ns()/1E6 # type: ignore
        # calculates duty cycle (%)
        duty_cycle_per = (servo.duty_ns()/MAX_PERIOD_NS)*100 # type: ignore

        #Prints the current duty cycle (%) and pulse width (ms)
        print('Servo Duty Cycle: {:.5f}% = {:.5f}ms'.format(duty_cycle_per, pulse_width_ms), end='\r')  # type: ignore

        # CPU waits for 10 ms till next iteration
        ## this allows the servo to get into position
        sleep_ms(10)
