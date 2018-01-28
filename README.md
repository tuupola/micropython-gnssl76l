# MicroPython GNSS L76-L I2C driver

MicroPython library for accessin the [Quectel GNSS L76-L](http://www.quectel.com/product/l76l.htm) receiver over I2C. L76-L is a
concurrent receiver module integrating GPS, GLONASS, Galileo and QZSS systems.

## Usage

Using default I2C pins for ESP32.

```python
import utime
from gnssl76l import GNSSL76L

receiver = GNSSL76L()
while True:
    for sentence in receiver.sentences():
        print(sentence)

    print("\n")
    utime.sleep_ms(1000)
```

Custom I2C pins when using non ESP32 board.

```python
import utime
from machine import I2C, Pin
from gnssl76l import GNSSL76L

i2c = I2C(scl=Pin(26), sda=Pin(25))
receiver = GNSSL76L(i2c)

while True:
    for sentence in receiver.sentences():
        print(sentence)

    print("\n")
    utime.sleep_ms(1000)
```

More realistic usage with timer. If you get `OSError: 26` or `i2c driver install error` after soft reboot do a hard reboot.

```python
import micropython
from machine import I2C, Pin, Timer
from gnssl76l import GNSSL76L

micropython.alloc_emergency_exception_buf(100)

i2c = I2C(scl=Pin(26), sda=Pin(25))
receiver = GNSSL76L(i2c)

def read_receiver(timer):
    for sentence in receiver.sentences():
        print(sentence)
    print("\n")

timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=read_receiver)
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.