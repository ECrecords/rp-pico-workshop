# Analog to Digital Converter (ADC)

Analog to digital converter (ADC) allow communication with the real world. Analog signals have continuously changing values which can measure sound, light, temperatures, and various other sources using sensors. 
 
An ADC will first sample & hold a current analog reading then it will quantize the analog sample, finally it will encode the quantized same.

<p align="center">
<img src="../../img/adc_block_inv.png" width="1000">
</p>


<p align="center">
<img src="../../img/adc_sig.jpg" width="650">
</p>

## class `ADC`

```python
def __init__(self, pin: Union[int, Pin], /):
    """
    Access the ADC associated with a source identified by *id*.  This
    *id* may be an integer (usually specifying a channel number), a
    :ref:`Pin <machine.Pin>` object, or other value supported by the
    underlying machine.
    """
```


###  `ADC` Class Functions

```python
```

## Demonstration
This section will show a on-board demonstration of using the `PWM` class. This demo will involve controlling a servo using a PWM signal.  
  
Wire your breadboards with the RP-RP2 to resemble the wiring diagram bellow.

![gpio_wiring](../../img/adc_demo.png)

### Follow the link and upload the code to your RP-RP2: [adc_demo.py](adc_demo.py)
