from machine import I2C, Pin
from AHT10 import AHT10

if __name__ == "__main__":
    # create an I2C object at GP3 and GP2
    i2c = I2C(id=1, scl=Pin(3), sda=Pin(2), freq=400000)  # type: ignore

    # create an AHT10 object
    sense = AHT10(i2c)

    print("Current Temperature and Relative Humidity")
    while True:
        print(
            "T: {:.3f} C, {:.3f} F \t RH: {}%".format(  sense.temperature_cel, 
                                                        sense.temperature_far, 
                                                        "TODO")
            , end='\r')