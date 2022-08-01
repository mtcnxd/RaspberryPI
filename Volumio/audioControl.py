import RPi.GPIO as GPIO
import alsaaudio as audio
from time import sleep

clk = 23
dt = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

scanCards = audio.cards()
#print("cards:", scanCards)

def volumeMasterUP():
    mixer = audio.Mixer('Headphone', cardindex=1)
    volume = mixer.getvolume()
    newVolume = int(volume[0])+1
    if newVolume <= 100:
        mixer.setvolume(newVolume)


def volumeMasterDOWN():
    mixer = audio.Mixer('Headphone', cardindex=1)
    volume = mixer.getvolume()
    newVolume = int(volume[0])-1
    if newVolume >= 0:
        mixer.setvolume(newVolume)


try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
                if dtState != clkState:
                    volumeMasterUP()
                    counter += 1
                else:
                    volumeMasterDOWN()
                    counter -= 1

                print counter
        clkLastState = clkState
        sleep(0.01)
finally:
        GPIO.cleanup()
