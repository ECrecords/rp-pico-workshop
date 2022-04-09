# Author: Elvis Chino-Islas
# Date: 4/9/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the UARTs on the
#   RP-RP2.

from machine import UART, Pin
import utime

# Declares a 32 byte buffer
read_bytes = bytearray(32)

# Declares and initializes UART0 using GP0 (TX) and GP1(RX)
uart0 = UART(id=0, baudrate=9600,tx=Pin(0), rx=Pin(1))


while True:
    if uart0.any() > 0:
        # Dump n bytes into buffer
        uart0.readinto(read_bytes, len(read_bytes))
        # Print the received bytes via REPL
        print(read_bytes.decode())
    
    # CPU sleeps for 1 ms
    utime.sleep_ms(1)
    

    
    

