#!/usr/bin/env python

from distutils.core import setup

setup(name='MFRC522',
    version='0.0.1',
    description='Raspberry Pi Python library for SPI RFID RC522 module.',
    install_requires=['spidev', 'RPi.GPIO'],
    packages=['MFRC522'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: POSIX :: Linux",
    ])
