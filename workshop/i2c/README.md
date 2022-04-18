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
def __init__(self, i2c: I2C, address: int = DEFAULT_ADDRESS) -> None:
    """
    This is the main function for allows access to the ATH10 chip. This will initalize
    the ATH10 object with taking an input of the I2C configuration.
    """
```
### `I2C` Imports
```python
from utime import sleep_ms
from machine import I2C, Pin
"""
    The utime module provides functions for getting the current time and date 
    measuring time intervals, and for delays. sleep_ms(x) is a method from
    utime that creates a delay for a given number of miliseconds, denoted
    by x.
    
    The machine module contains specific functions related to the hardware on a      
    particular board. I2C allows for the setup of the I2C protocol. Pin gives access 
    to the GPIO pin that is associaed with a given id.
"""
```

### `I2C` Constants
```python
    DEFAULT_ADDRESS = 0x38
    INITIALIZATION = bytearray([0xE1, 0x08, 0x00])
    TRIGGER_MEASUREMENT = bytearray([0xAC, 0x33, 0x00])
    SOFT_RESET = bytearray([0xBA])

    NUM_DATA_BYTES = 6
    MEASUREMENT_WAIT = 75
    SOFT_RESET_WAIT = 20
```


### `I2C` Class Functions
```python
    def __trigger_measurements(self):
        self.i2c.writeto(self.address, self.TRIGGER_MEASUREMENT)
        sleep_ms(self.MEASUREMENT_WAIT)

    """
    trigger_measurements:
    - Write TRIGGER_MEASUREMENT byte array to I2C bus
    - Sleep for 75 ms as the sensor conducts measurements
    """
    def __raw_measure(self):
        return self.i2c.readfrom(self.address, self.NUM_DATA_BYTES)
    """
    raw_measure:
    - Used to read raw byte data from sensor
    - Read 6 bytes form I2C device
    """
    def soft_reset(self):
        self.i2c.writeto(self.address, self.SOFT_RESET)
        sleep_ms(self.SOFT_RESET_WAIT)
    """
    soft_reset:
    - Used to reset the sensor
    - Write SOFT_RESET byte array to I2C bus
    - Sleep for 20 ms as sensor resets
    """
    @property
    def temperature_cel(self):
        self.__trigger_measurements()
        raw_data = self.__raw_measure()
        temp_data =  ((raw_data[3] & 0x0F) << 16) | (raw_data[4] << 8 ) |  (raw_data[5])
        return (temp_data/(2**20))*200-50
    
    """
    temperature_cel:
    - Used to get a current measurement of the temperature in celsius
    - Trigger sensor measurement
    - Get a raw measurement
    - Isolate temperature data using bit manipulation
    - Convert data to celsious using temperature transform form AHT10 documentation
    """
    
    @property
    def temperature_far(self):
        cel_temp = self.temperature_celt
        return cel_temp * (9/5) + 32
    """
    temperature_far:
    - Used to get a current measurement of the temperature in fahrenheit
    - Get a current temperature in celsius
    - Convert to fahrenheit
    """
    @property
    def rel_humidity(self):
        pass
    """
    rel_humidity:
    - Read raw_data from the sensor and isolate the humidity data using bit         
    manipulation then use the relative humidity transforamtion from the AHT10 
    documentation to get the data into a "human" format.
    """
```
## Demonstration

![i2c_wiring](../../img/i2c_demo_bb.png)

### Follow the lin and upload the code to your RP-RP2: [i2c_demo.py](../i2c/i2c_demo.py)