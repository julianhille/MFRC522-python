#!/usr/bin/env python3

import RPi.GPIO as GPIO
import SimpleMFRC522
import signal
import sys
import time
import requests

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
    if text:
      response = requests.get('http://localhost:3689/api/player')
      response.json()
      requests.put('http://localhost:3689/api/player/stop')
      requests.put('http://localhost:3689/api/queue/clear')
      requests.put('http://localhost:3689/api/player/shuffle?state=false')
      requests.put('http://localhost:3689/api/player/repeat?state=off')
      response = requests.post('http://localhost:3689/api/queue/items/add?uris=' + text)
      requests.put('http://localhost:3689/api/player/play')
    time.sleep(1)
finally:
  GPIO.cleanup()
