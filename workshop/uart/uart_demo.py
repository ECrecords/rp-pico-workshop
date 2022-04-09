# Author: Elvis Chino-Islas
# Date: 4/9/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the UARTs on the
#   RP-RP2.

from machine import UART, Pin
import utime

baud = 9600

# Declares a 32 byte buffer
read_bytes = bytearray(32)

# Declares and initializes UART0 using GP0 (TX) and GP1(RX)
tx_flag = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
rx_flag = Pin(3, mode=Pin.IN, pull=Pin.PULL_DOWN)

uart0 = UART(id=0, baudrate=baud,tx=Pin(0), rx=Pin(1))

while True:

    if tx_flag:
        # Ask for string via REPL
        outp_str = input("UART Message: ")

        # Encodes string (ASCII)
        write_bytes = outp_str.encode()

        # Writes message via GP0
        uart0.write(write_bytes)

        # CPU sleeps for msg to be fully sent
        utime.sleep_ms( round( (len(outp_str)/9600) * 1E3) )
    

    if rx_flag:
        if uart0.any() > 0:
            # Dump n bytes into buffer
            uart0.readinto(read_bytes, len(read_bytes))
            # Print the received bytes via REPL
            print(read_bytes.decode())

    # CPU sleeps for 1 ms
    utime.sleep_ms(1)


    
    
    

    
    

