from machine import UART, Pin
import utime

# Declares a 32 byte buffer
write_bytes = bytearray(32)

# Declares and intiaizares UART0 using GP0 (TX) and GP1(RX)
uart0 = UART(id=0, baudrate=9600,tx=Pin(0), rx=Pin(1))

while True:

    # Ask for string via REPL
    outp_str = input("UART Message: ")

    # Encodes string (ASCII)
    write_bytes = outp_str.encode()

    # Writes message via GP0
    uart0.write(write_bytes)

    # CPU sleeps for msg to be fully sent
    utime.sleep_ms(5)

