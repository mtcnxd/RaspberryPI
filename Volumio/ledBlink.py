# Habilitar GPIO
# sudo apt-get install python-dev
# sudo apt-get install python-rpi.gpio
# Habilitar i2c
# sudo apt-get install python-smbus

import RPi.GPIO as GPIO
import time

PIN = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

while True:
	GPIO.output(PIN, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(PIN, GPIO.LOW)
	time.sleep(0.5)
