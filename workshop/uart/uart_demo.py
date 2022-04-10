# Author: Elvis Chino-Islas
# Date: 4/9/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the UARTs on the
#   RP-RP2.

from machine import UART, Pin
import utime

# Rate at which UART communicates (bits per second)
BAUD = 9600
# Num of START bits
START_BITS = 1
# Num of STOP bits
STOP_BITS = 1
# Num of PARITY bits
PARITY_BITS = 0
# PARITY bit type
PARITY_TYPE = None
# BAUD rate converted to bytes per second
BYTES_PER_SEC = 1/(BAUD/8)

# Declares a 32 byte buffer
write_bytes = bytearray()
read_bytes = ""

# Declares and initializes UART0 using GP0 (TX) and GP1(RX)
tx_flag = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
rx_flag = Pin(3, mode=Pin.IN, pull=Pin.PULL_DOWN)

uart0 = UART(id=0, baudrate=BAUD, stop=STOP_BITS, tx=Pin(0), rx=Pin(1))

while True:

    if tx_flag:
        # Ask for string via REPL
        output_str = input("UART Message: ")
        write_bytes = bytearray(len(output_str))
        # Encodes string (ASCII)
        write_bytes = output_str.encode()

        # Writes message via GP0
        uart0.write(write_bytes)

        # Calculates amount of time CPU must wait for UART to fully send message
        sleep_time = BYTES_PER_SEC * (START_BITS + len(write_bytes) + PARITY_BITS + STOP_BITS)
        # CPU sleeps for msg to be fully sent
        utime.sleep_ms(round(sleep_time * 1E3))
    

    if rx_flag:
        if uart0.any() > 0:
            # Dump n bytes into buffer
            uart0.readline()
            # Print the received bytes via REPL
            print(read_bytes)

    # CPU sleeps for 1 ms
    utime.sleep_ms(1)