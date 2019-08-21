# Access to this file : ZoneRepresentative
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print('Looking for Voter-IDs')

try:
    id = reader.read()
    print(id)
finally:
    GPIO.cleanup()
