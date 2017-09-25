# MicroPython GNSS L76-L I2C driver

MicroPython library for accessin the [Quectel GNSS L76-L](http://www.quectel.com/product/l76l.htm) receiver over I2C. L76-L is a
concurrent receiver module integrating GPS, GLONASS, Galileo and QZSS systems.

## Usage

Using default I2C pins for ESP32.

```python
import utime
from gnssl76l import GNSSL76L

gps = GNSSL76L()
while True:
    for sentence in gps.sentences():
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
gps = GNSSL76L(i2c)

while True:
    for sentence in gps.sentences():
        print(sentence)

    print("\n")
    utime.sleep_ms(1000)
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.