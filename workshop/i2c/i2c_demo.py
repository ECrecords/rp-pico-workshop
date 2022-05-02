# Author: Elvis Chino-Islas
# Date: 4/22/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the I2C on the
#   RP-RP2 by controling a temperature and humidity sensor (AHT10)

from machine import I2C, Pin
from aht10 import AHT10
from ssd1306 import SSD1306_I2C
from micropython import const
import framebuf

# Defines a function that will read image data from
## text file and return it as a bytearray
def image_data():
    buffer = bytearray()
    with open("img_data.txt", "r") as img:
        for line in img:
            line = line.strip(", \n")
            line = line.replace(" ", "")
            line = line.replace("0x", "")
            line = line.split(",")
            for i in line:
                buffer.append(int(i, 16))
    return buffer

if __name__ == "__main__":
    # create an I2C object at GP3 and GP2
    i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=400000)  # type: ignore

    # scan the i2c bus and store all device addresses into list
    i2c_dev = i2c.scan()

    # print all address found in the i2c bus onto REPL
    print("Device on I2C bus:", end=" ")
    for dev in i2c_dev:
        print(hex(dev), end=' ')
    print("\n")

    # create an AHT10 object
    sense = AHT10(i2c)

    #TODO create an SSD1306_I2C object and initialize it
    
    #TODO clear the display

    # display current temperature and rh onto REPL
    print("Current Temperature and Relative Humidity")
    while True:
        print(
            "T: {:.3f} C, {} F \t RH: {}%".format(  sense.temperature_cel, 
                                                        "TODO", 
                                                        "TODO")
            , end='\r')

        #TODO display image and selected data
        ## assign button(s) to display either cel, far, or rh