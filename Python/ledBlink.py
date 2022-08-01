#!/usr/bin/python

import RPi.GPIO as GPIO
import time

ledPin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

# Realiza un parpadeo del LED
def blink():   
    for i in range(5):
        GPIO.output(ledPin, True)
        time.sleep(0.5)
        GPIO.output(ledPin, False)
        time.sleep(0.5)
        
# Ciclo infinito para la verificacion del correo
while True:
    blink()
    time.sleep (1)
