#!/usr/bin/env python3

import RPi.GPIO as GPIO
from MFRC522 import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    reader.wait_for_tag()
    id, text = reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()
