#import hardware used in design
## i.e from machine import UART

########## Declare and initialize global variables ##########

##TODO Declare Pins with as inputs and pull them up
### i.e pin = Pin(N, mode=Pin.IN, pull=Pin.PULL_UP)


##TODO Declare timer and bool to keep track of existence

#TODO Declare global variables used in interrupts

##TODO Declare update flag and set to false

##TODO Declare option 

##TODO Declare mode, min, sec, hsec and initialize them

################ Interrupt Service Routines #################

##TODO Implement Timer ISR
def handler(callback_ref):
    pass # REMOVE

##TODO Implement Pin ISRs for each button
def start_handler(callback_ref):
    pass # REMOVE

def pause_handler(callback_ref):
    pass # REMOVE

def reset_handler(callback_ref): 
    pass # REMOVE

def stop_handler(callback_ref):
    pass # REMOVE

###################### Option Functions #####################

##TODO Implement start
def start():
    pass # REMOVE

##TODO Implement pause
def pause():
    pass # REMOVE
    
##TODO Implement reset
def reset():
    pass #REMOVE

##TODO Implement stop
def stop():
    pass # REMOVE

############################ Main ###########################

if __name__ == '__name__':

    ##TODO set irq for each Pin
    ### i.e pin.irq(handler=pin_handler, trigger=Pin.IRQ_FALLING)

    switch = {
        1: start,
        2: pause,
        3: reset,
        4: stop
    }

    while True:
        pass # REMOVE
        #UNCOMMENT - use this to call option functions
        # if (callable(switch.get(option))):
        #     switch.get(option)()
        #     option = 0

        ##TODO create logic to update min, sec, hsec, and mode
        
        #UNCOMMENT - use this to print
        #print('{}: {}:{}:{}'.format(mode, min, sec, hsec), end='\r')
        
        ##TODO sleep for 5 ms to prevent over utilization

#############################################################