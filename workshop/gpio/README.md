# General Purpose Input/Output
## Introduction
### class `Pin`

A pin object is used to control ***general purpose input/output*** (GPIO) pins. `Pin` objects are associated with physical pins on the RP-RP2 as seen in the pin-out diagram.

<p align="center">
    <img src="../../img/Pico-R3-SDK11-Pinout.png" alt="pico_pinout" width="600">
    <br> <b> Raspberry Pi Pico Pinout </b>
</p>

### Initializing A `Pin` Object

Initialization of a Pin object is done when declaring it. The default constructor's signature can be seen below.

```python
def __init__(self, id: Union[int, str], /, mode: int = IN, pull: int = PULL_UP, af: Union[str, int] = -1):
```

Below is an example of creating a instance of a `Pin` object at GP0 as an input while being pulled down.

```python
from machine import Pin
...
pin = Pin(0, mode.Pin.IN, pull=Pin.PULL_DOWN)
```

### `Pin` Class Attributes
Bellow are the class attributes of the `Pin` object available on the RP-RP2.

```python
class Pin:
    ...
    ALT = 3
    IN = 0
    IRQ_FALLING = 4
    IRQ_RISING = 8
    OPEN_DRAIN = 2
    OUT = 1
    PULL_DOWN = 2
    PULL_UP = 1
    ... 
```

They are accessed in the following way: `Pin.IRQ_FALLING`





## [Python Code](gpio_demo.py)

## Wiring Diagram
![gpio_wiring](../../img/gpio_demo.png)