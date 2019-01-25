# MFRC522-python
Library for interfacing with the NFC reader Module MFRC522 on the Raspberry Pi.

`mfrc522.py` is a python port of the "Arduino RFID Library for MFRC522" (https://github.com/miguelbalboa/rfid).
Additionally some code is based on [mxgxw/MFRC522-python](https://github.com/mxgxw/MFRC522-python), [ondryaso/pi-rc522](https://github.com/ondryaso/pi-rc522)
and [pimylifeup/MFRC522-python](https://github.com/pimylifeup/MFRC522-python).

There is a lot of documentation available at https://github.com/miguelbalboa/rfid with useful hints and informations.

__NOTE__: This is still work in progress and greatly untested! Use at own risk!

`simple_mfrc522.py` is a small utility class to simplify interaction with the MFRC522.


## What works?
Working:

- Communication (Crypto1) with MIFARE Classic 1k
- Communication with MIFARE Ultralight
- Firmware self check of MFRC522


## Pins

| Name   | Physical pin # | BCM pin #    |
|:------:|:--------------:|:------------:|
| SDA    | 24             | GPIO8        |
| SCK    | 23             | GPIO11       |
| MOSI   | 19             | GPIO10       |
| MISO   | 21             | GPIO9        |
| IRQ    | None           | None         |
| GND    | 6, 9, 20, 25   | Ground       |
| RST    | 22             | GPIO25       |
| 3.3V   | 1,17           | 3V3          |


## Requirements
This library depends on the following libraries:

- [spidev](https://pypi.python.org/pypi/spidev)
- [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)


## Installation
Install from GIT:

```
git clone https://github.com/chme/MFRC522-python.git
cd MFRC522-python
python3 setup.py install
```


## Usage
Take a look at the examples.

**Logging:**

The following loggers are used enumerated by names:

- 'mfrc522.log':     Log errors and warnings
- 'mfrc522.trace':   Log method calls and steps (verbose)
- 'mfrc522.spi':     Log SPI communication (very verbose)

You may subscribe to these loggers for getting logging messages.


## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.

