import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="micropython-gnssl76l",
    py_modules=["gnssl76l"],
    version="0.1.0",
    description="MicroPython I2C driver for the Quectel GNSS L76-L (GPS) receiver",
    long_description="L76-L is a concurrent receiver module integrating GPS, GLONASS, Galileo and QZSS systems. This library communicates uses I2C to access the L76-L.",
    keywords="gps glonass galileo qzss micropython i2c",
    url="https://github.com/tuupola/micropython-gnssl76l",
    author="Mika Tuupola",
    author_email="tuupola@appelsiini.net",
    maintainer="Mika Tuupola",
    maintainer_email="tuupola@appelsiini.net",
    license="MIT",
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)