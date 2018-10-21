#!/usr/bin/env python3

import RPi.GPIO as GPIO
from MFRC522 import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    text = input('New data:')
    print("Now place your tag to write")
    reader.wait_for_tag()
    id, uid = reader.read_id()
    reader.write(uid, text)
    print("Written")
finally:
    GPIO.cleanup()
