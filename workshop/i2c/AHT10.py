from utime import sleep_ms
from machine import I2C, Pin

class AHT10:
    DEFAULT_ADDRESS = 0x38
    INITIALIZATION = bytearray([0xE1, 0x08, 0x00])
    TRIGGER_MEASUREMENT = bytearray([0xAC, 0x33, 0x00])
    SOFT_RESET = bytearray([0xBA])

    def __init__(self, i2c: I2C, address: int = DEFAULT_ADDRESS) -> None:

        if i2c == None:
            raise ValueError("Requires I2C Object")

        self.i2c = i2c
        self.address = address

        if self.address not in self.i2c.scan():
            raise ValueError("AHT10 Not Found")

        self.i2c.writeto(self.address, self.INITIALIZATION)

    def __trigger_measurements(self):
        self.i2c.writeto(self.address, self.TRIGGER_MEASUREMENT)
        sleep_ms(75)

    def __raw_measure(self):
        return self.i2c.readfrom(self.address, 6)

    def soft_reset(self):
        self.i2c.writeto(self.address, self.SOFT_RESET)

    @property
    def temperature_cel(self):
        self.__trigger_measurements()
        raw_data = self.__raw_measure()
        temp_data =  ((raw_data[3] & 0x0F) << 16) | (raw_data[4] << 8 ) |  (raw_data[5])
        return (temp_data/(2**20))*200-50
    
    @property
    def temperature_far(self):
        cel_temp = self.temperature_cel
        return cel_temp * (9/5) + 32

    @property
    #TODO Read raw_data from the sensor using bit manipulation
    # then use the relative humidity transforamtion from the AHT10 documention
    # to get the data into a "human" format
    def rel_humidity(self):
        pass


if __name__ == "__main__":
    i2c = I2C(id=1, scl=Pin(3), sda=Pin(2), freq=400000)  # type: ignore
    sense = AHT10(i2c)

    print("Current Temperature and Relative Humidity")
    while True:
        print("T: {:.3f} C, {:.3f} F \t RH: {}%".format(sense.temperature_cel, sense.temperature_far, "TODO"), end='\r')
        
