# Author: Elvis Chino-Islas
# Date: 4/17/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the I2C on the
#   RP-RP2 by controling a temperature and humidity sensor (AHT10)

from utime import sleep_ms
from machine import I2C, Pin

class AHT10:

    # Class Constants
    DEFAULT_ADDRESS = 0x38
    INITIALIZATION = bytearray([0xE1, 0x08, 0x00])
    TRIGGER_MEASUREMENT = bytearray([0xAC, 0x33, 0x00])
    SOFT_RESET = bytearray([0xBA])

    NUM_DATA_BYTES = 6
    MEASUREMENT_WAIT = 75
    SOFT_RESET_WAIT = 20

    # Default Constructor
    def __init__(self, i2c: I2C, address: int = DEFAULT_ADDRESS) -> None:

        # If I2C object exists and it is of I2C type
        if i2c == None or I2C != type(i2c):
            raise ValueError("Requires I2C Object")

        self.i2c = i2c
        self.address = address

        # Checks if there is a valid I2C device at 
        ## given address
        if self.address not in self.i2c.scan():
            raise ValueError("AHT10 Not Found")

        # Write INITIALIZATION byte array onto the I2C bus
        self.i2c.writeto(self.address, self.INITIALIZATION)

    # used to initiate a measurement on the AHT10 sensor
    def __trigger_measurements(self):
        # Write TRIGGER_MEASUREMENT byte array to I2C bus
        self.i2c.writeto(self.address, self.TRIGGER_MEASUREMENT)
        # Sleep for 75 ms as the sensor conducts measurements
        sleep_ms(self.MEASUREMENT_WAIT)

    # used to read raw byte data from sensor
    def __raw_measure(self):
        # Read 6 bytes form I2C device
        return self.i2c.readfrom(self.address, self.NUM_DATA_BYTES)

    # used to reset the sensor
    def soft_reset(self):
        # Write SOFT_RESET byte array to I2C bus
        self.i2c.writeto(self.address, self.SOFT_RESET)
        # Sleep for 20 ms as sensor resets
        sleep_ms(self.SOFT_RESET_WAIT)

    # used to get a current measurement of the temperature in celsius
    @property
    def temperature_cel(self):
        # trigger sensor measurement
        self.__trigger_measurements()
        # get a raw measurement
        raw_data = self.__raw_measure()
        # isolate temperature data using bit manipulation
        temp_data =  ((raw_data[3] & 0x0F) << 16) | (raw_data[4] << 8 ) |  (raw_data[5])
        # convert data to celsious using temperature transform form AHT10 documentation
        return (temp_data/(2**20))*200-50
    
    # used to get a current measurement of the temperature in fahrenheit
    @property
    def temperature_far(self):
        # get a current temperature in celsius
        cel_temp = self.temperature_cel
        # convert to fahrenheit
        return cel_temp * (9/5) + 32

    #TODO Read raw_data from the sensor and isolate the humidity data using bit manipulation
    # then use the relative humidity transforamtion from the AHT10 documentation
    # to get the data into a "human" format
    @property
    def rel_humidity(self):
        pass


if __name__ == "__main__":
    # create an I2C object at GP3 and GP2
    i2c = I2C(id=1, scl=Pin(3), sda=Pin(2), freq=400000)  # type: ignore

    # create an AHT10 object
    sense = AHT10(i2c)

    print("Current Temperature and Relative Humidity")
    while True:
        print("T: {:.3f} C, {:.3f} F \t RH: {}%".format(sense.temperature_cel, sense.temperature_far, "TODO"), end='\r')