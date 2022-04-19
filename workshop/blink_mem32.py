# Author: Elvis Chino-Islas
# Date: 4/19/2020
# Purpose: RP-RP2 Workshop
# Description:
#   Demonstrate how to use the GPIO using mem32

from machine import mem32

# User Bank IO registers base address
IO_BANK0_BASE = 0x4001_4000

#GP25 control register offset
GPIO25_CTRL_OFFSET = 0x0cc

# Masks used to isolate fields 
## of the control register
CTRL_REG_IRQOVER_MASK = 0x3000_0000
CTRL_REG_INOVER_MASK = 0x3_0000
CTRL_REG_OEOVER_MASK = 0x3000
CTRL_REG_OUTOVER_MASK = 0x300
CTRL_REG_FUNCSEL_MASK = 0x1F

# Used to set FUNCSEL field to SIO
CTRL_REG_FUNCSEL_SIO = 0x5

# Store the contents of GP25 control register
gpio25_ctrl_reg = mem32[IO_BANK0_BASE + GPIO25_CTRL_OFFSET] # type: ignore

# Clear all the fields using a combinations of masks
gpio25_ctrl_reg &= ~( CTRL_REG_IRQOVER_MASK | CTRL_REG_INOVER_MASK | 
    CTRL_REG_OEOVER_MASK | CTRL_REG_OUTOVER_MASK | CTRL_REG_FUNCSEL_MASK)

# Set the FUNCSEL field to SIO
gpio25_ctrl_reg |= CTRL_REG_FUNCSEL_SIO

# Store the manipulated data back to GP25 control register
mem32[IO_BANK0_BASE + GPIO25_CTRL_OFFSET] = gpio25_ctrl_reg # type: ignore

#TODO use the RP2040 to turn on the on-board LED
## Use Chapter 2.3.1.2. GPIO Control