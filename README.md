# MFRC522-python
Library for interfacing with the NFC reader Module MFRC522 on the Raspberry Pi.

`mfrc522.py` is a python port of the "Arduino RFID Library for MFRC522" (https://github.com/miguelbalboa/rfid).
Additionally some code is based on [mxgxw/MFRC522-python](https://github.com/mxgxw/MFRC522-python), [ondryaso/pi-rc522](https://github.com/ondryaso/pi-rc522)
and [pimylifeup/MFRC522-python](https://github.com/pimylifeup/MFRC522-python).

There is a lot of documentation available at https://github.com/miguelbalboa/rfid with useful hints and informations.

__NOTE__: This is still work in progress and not all ported functions are verified working. Use at own risk!

`simple_mfrc522.py` is a small utility class to simplify interaction with the MFRC522.


## What works?
Working:

- Communication (Crypto1) with MIFARE Classic 1k
- Communication with MIFARE Ultralight
- Firmware self check of MFRC522


## Pins

| Name   | Physical pin # | BCM pin #    |
| ------ | --------------:| ------------ |
| SDA    | 24             | GPIO8        |
| SCK    | 23             | GPIO11       |
| MOSI   | 19             | GPIO10       |
| MISO   | 21             | GPIO9        |
| IRQ    | 18             | GPIO24       |
| GND    | 6, 9, 20, 25   | Ground       |
| RST    | 22             | GPIO25       |
| 3.3V   | 1,17           | 3V3          |


## Requirements
This library requires Python 3 and depends on the following libraries:

- [spidev](https://pypi.python.org/pypi/spidev)
- [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)


## Installation
Install from GIT:

```shell
git clone https://github.com/chme/MFRC522-python.git
cd MFRC522-python
python3 setup.py install
```


## Usage

This repository includes a couple of [examples](https://github.com/chme/MFRC522-python/tree/master/examples) showing how to read, write, and dump data from a chip. Also take a look at the source code documentation in for `MFRC522` and `SimpleMFRC522`.

Example program showing how to use `MFRC522` to detect a card and dump its contents to stdout:

```python
from mfrc522 import MFRC522

rfid = MFRC522()
rfid.pcd_init()                     # Init MFRC522
rfid.pcd_dump_version_to_serial()   # Show details of PCD - MFRC522 Card Reader details

while True:
    sleep(1)

    # Look for new cards
    if not rfid.picc_is_new_card_present():
        continue

    # Select one of the cards
    result, uid = rfid.picc_read_card_serial()
    if not result:
        continue

    # Dump debug info about the card
    print('New PICC')
    rfid.picc_dump_to_serial(uid)
```


Example program showing how to use `SimpleMFRC522` to detect a card and dump its data decoded as utf-8 to stdout:

```python
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()
rfid.init()                               # Init MFRC522

while True:
    status, uid, text = rfid.read_text()  # Blocks until a readable tag is present (assumes that data on the tag is utf-8 encoded text

    print('New PICC')
    print(text)

    rfid.wait_for_card_removed()          # Blocks until all tags are removed from the RFID reader
```


**Logging**

This library uses standard python logging. 
The following loggers are used enumerated by names:

| Logger name      | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| mfrc522.log      | Log errors and warnings                                          |
| mfrc522.trace    | Log method calls and steps (verbose - logs only in DEBUG level)  |
| mfrc522.spi      | Log SPI communication (very verbose - logs only in DEBUG level)  |

You may subscribe to these loggers for getting logging messages.


## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.

