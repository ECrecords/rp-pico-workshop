# Inter-Integrated Circuit (I<sup>2</sup>C)

Inter-Integrated Circuit (I<sup>2</sup>C), also known as I2C, is a bus interface connection protocol that is incorporated into devices for serial communication. This protocol is used to connect microcontrollers, EEPROMS, converters and I/O interfaces in embedded systems. It allows for short-distance communciation among devices.

The I2C has two bi-direction lines for data communcation called <b>SDA</b> and <b>SCL</b>.

<b>SDA</b>
<br>
The Serial Clock, SCL, carries the clock signal.

<b>SCL</b>
<br>
The Serial Data, SDA, is where the transfer of data occurs.

Alongside the SCL and SDA, there are two operating modes.
<ul>
    <li> <b>Master</b> - SCL resides here.
    <li> <b>Slave</b> - Has bidirectional SDA communcation with Master
</ul>

<p align="center">
<img src="../../img/i2c_master_slave.png" width="425">
</p>

## AHT10 Overview
The AHT10 is equipped with an ASIC chip that communcations with temperature and hunidity seniors. It uses the I2C protocol to calibrate the digial output signals. This is what we will be using to communicate with the Raspberry Pi Pico to allow for the reading of the temperature and humidity of the atmosphere.

The following images, Figure A and Figure B, shows the distribution of pins and a typical circuit with the AHT10 with master. We will be making a circuit similar to the one in Figure B to allow to read the temperature and humidity of the atmosphere.

<p align="center">
<img src="../../img/i2c_aht10_diagram.png" width="400">
<br>
<i>Figure A</i>
</p>

<p align="center">
<img src="../../img/i2c_aht10_master_to_chip.png" width="400">
<br>
<i>Figure B</i>
</p>


## class `I2C`
```python
from machine import I2C
i2c = I2C(freq=400000)
i2c.scan()                     
i2c.writeto(42, b'123')         
i2c.readfrom(42, 4)             
i2c.readfrom_mem(42, 8, 3)
i2c.writeto_mem(42, 2, b'\x10') 
```

The following table shows the defauly I2C pins for the Raspberry Pi Pico.
<p align="center">
<img src="../../img/i2c_default_pins_figure.png" width="600">
<br>
<i>Table A</i>
</p>

### `I2C` Class Functions
```python
I2C.init(scl, sda, *, freq=400000)
"""
Initialise the I2C bus with the given arguments:
    - scl is a pin object for the SCL line
    - sda is a pin object for the SDA line
    - freq is the SCL clock rate
"""
def I2C.deinit()
"""
Turn off the I2C bus.
"""
def I2C.scan()
"""
Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of those that respond. A device responds if it pulls the SDA line low after its address (including a write bit) is sent on the bus.
"""
def I2C.start()
"""
Generate a START condition on the bus (SDA transitions to low while SCL is high).
"""
def I2C.stop()
"""
Generate a STOP condition on the bus (SDA transitions to high while SCL is high).
"""

def I2C.readinto(buf, nack=True, /)
"""
Reads bytes from the bus and stores them into buf. The number of bytes read is the length of buf. An ACK will be sent on the bus after receiving all but the last byte. After the last byte is received, if nack is true then a NACK will be sent, otherwise an ACK will be sent (and in this case the peripheral assumes more bytes are going to be read in a later call).
"""
def I2C.write(buf)
"""
Write the bytes from buf to the bus. Checks that an ACK is received after each byte and stops transmitting the remaining bytes if a NACK is received. The function returns the number of ACKs that were received.
"""
def I2C.readfrom(addr, nbytes, stop=True, /)
"""
Read nbytes from the peripheral specified by addr. If stop is true then a STOP condition is generated at the end of the transfer. Returns a bytes object with the data read.
"""

def I2C.readfrom_into(addr, buf, stop=True, /)
"""
Read into buf from the peripheral specified by addr. The number of bytes read will be the length of buf. If stop is true then a STOP condition is generated at the end of the transfer.

The method returns None.
"""
def I2C.writeto(addr, buf, stop=True, /)
"""
Write the bytes from buf to the peripheral specified by addr. If a NACK is received following the write of a byte from buf then the remaining bytes are not sent. If stop is true then a STOP condition is generated at the end of the transfer, even if a NACK is received. The function returns the number of ACKs that were received.
"""

def I2C.writevto(addr, vector, stop=True, /)
"""
Write the bytes contained in vector to the peripheral specified by addr. vector should be a tuple or list of objects with the buffer protocol. The addr is sent once and then the bytes from each object in vector are written out sequentially. The objects in vector may be zero bytes in length in which case they don’t contribute to the output.

If a NACK is received following the write of a byte from one of the objects in vector then the remaining bytes, and any remaining objects, are not sent. If stop is true then a STOP condition is generated at the end of the transfer, even if a NACK is received. The function returns the number of ACKs that were received.
"""

def I2C.readfrom_mem(addr, memaddr, nbytes, *, addrsize=8)
"""
Read nbytes from the peripheral specified by addr starting from the memory address specified by memaddr. The argument addrsize specifies the address size in bits. Returns a bytes object with the data read.
"""

def I2C.readfrom_mem_into(addr, memaddr, buf, *, addrsize=8)
"""
Read into buf from the peripheral specified by addr starting from the memory address specified by memaddr. The number of bytes read is the length of buf. The argument addrsize specifies the address size in bits (on ESP8266 this argument is not recognised and the address size is always 8 bits).

The method returns None.
"""

def I2C.writeto_mem(addr, memaddr, buf, *, addrsize=8)
"""
Write buf to the peripheral specified by addr starting from the memory address specified by memaddr. The argument addrsize specifies the address size in bits (on ESP8266 this argument is not recognised and the address size is always 8 bits).

The method returns None.
"""
```
## Demonstration

![i2c_wiring](../../img/i2c_demo_bb.png)

### Follow the lin and upload the code to your RP-RP2: [i2c_demo.py](../i2c/i2c_demo.py)