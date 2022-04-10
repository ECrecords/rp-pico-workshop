# Universal Asynchronous Receiver Transmitter (UART)

## Introduction
Universal asynchronous receiver transmitter (UART) is a serial commination protocol that is used to communicate between any two devices.
It is an asynchronous protocol, therefore is has no need for a clock. It utilizes only two connections to function. UART delivers a message using a 11/12 bit packet. The frame can be seen bellow.

<p align="center">
<img src="../../img/uart_dark.png" width="800">
<br> <b> UART Frame </b>
</p>

When design a application that utilizes UART the following parameters must be considered:
- `START` bit
- `DATA` byte
- `PARITY` bit (optional)
- `STOP` bit


## [Python Code](uart_demo.py)
## Wiring Diagram
![uart_wiring](../../img/uart_demo_bb.png)