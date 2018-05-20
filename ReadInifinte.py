#!/usr/bin/env python3

import RPi.GPIO as GPIO
import SimpleMFRC522
import signal
import sys
import time

run = True
reader = SimpleMFRC522.SimpleMFRC522()

def end_read(signal, frame):
  global run
  print("\nCtrl+C captured, ending read.")
  run = False
  sys.exit()

signal.signal(signal.SIGINT, end_read)

try:
  while run:
    id, text = reader.read()
    print("\nNew card detected:")
    print(id)
    print(text)
    time.sleep(1)
finally:
  GPIO.cleanup()
