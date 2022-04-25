# Hardware Timers & Watchdog Timers (WDT)

## class `Timer`

### Initializing A `Timer` Object

### `Timer` Class Functions



## class `WDT`

### Initializing A `WDT` Object

A WDT object must be initiated when declaring and cannot be modified in any
way.

```python
def __init__(self, *, id: int = 0, timeout: int = 5000):
      """
      Create a WDT object and start it. The timeout must be given in milliseconds.
      Once it is running the timeout cannot be changed and the WDT cannot be stopped either.
      """
```
### `WDT` Class Functions

The WDT class a single function shown bellow:

```python
def feed(self) -> None:
    """
    Feed the WDT to prevent it from resetting the system. The application
    should place this call in a sensible place ensuring that the WDT is
    only fed after verifying that everything is functioning correctly.
    """
```


## WDT Demonstration
## [Python Code](wdt_demo.py)

## Hardware Timer Demostration

## [Python Code](oop_stopwatch.py)

## [Write Your Own Stopwatch](stopwatch_template.py)

