# Author: Elvis Chino-Islas
# Date: 4/9/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the UARTs on the
#   RP-RP2.

from machine import UART, Pin
import utime
from micropython import const

# Rate at which UART communicates (bits per second)
BAUD            = const(9600)
# Num of START bits
START_BITS      = const(1)
# Num of STOP bits
STOP_BITS       = const(1)
# Num of PARITY bits
PARITY_BITS     = const(0)
# PARITY bit type
PARITY_TYPE     = None
# BAUD rate converted to bytes per second
BYTES_PER_SEC   = 1/(BAUD/8)

if __name__ == '__main__':

    # Declares a 32 byte buffer
    write_bytes = bytearray()
    read_bytes = bytearray()

    # Declare and initialize RX trigger
    is_rx = False

    # Declares and initializes UART0 using GP0 (TX) and GP1(RX)
    uart0 = UART(0, tx=Pin(0), rx=Pin(1))

    #   Declare and initializes flags that enable RX and TX independently
    tx_flag = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
    rx_flag = Pin(3, mode=Pin.IN, pull=Pin.PULL_DOWN)

    while True:

        # if GP2 is high
        if tx_flag.value():
            # Ask for string via REPL
            output_str = input("UART Message: ")
            write_bytes = bytearray(len(output_str))

            # Encodes string (ASCII)
            write_bytes = bytearray(output_str.encode())

            # Writes message via GP0
            uart0.write(write_bytes)

            # Calculates amount of time CPU must wait for UART to fully send message
            sleep_time = BYTES_PER_SEC * (len(output_str))
            # CPU sleeps for msg to be fully sent
            utime.sleep_ms(round(sleep_time * 1E3))
        
        # if GP2 is low
        if rx_flag.value():

            #print('Receiving: ', end='')

            # Clear read buffer
            read_bytes = bytes()

            # While UART has bytes waiting
            while uart0.any() > 0:
                # set rx trigger
                is_rx = True

                # append read byte to buffer
                read_bytes += uart0.read(1) #type: ignore
            
            # If something was received
            if is_rx:
                # Clear rx trigger
                is_rx = False

                # Print received message
                print(read_bytes.decode())
            
            utime.sleep_ms(round((BYTES_PER_SEC * 256) * 1E3))
            
        # CPU sleeps for 1 ms
        utime.sleep_ms(1)