#!/usr/bin/env python

#Se importa el objeto SMBus
from smbus import SMBus
#Se importa la funcion sleep y se renombra a delay, la funcion delay hace una espera medida segundos
from time import sleep as delay

import sys

#Se establecen los valores para HIGH y LOW, los cuales encienden y apagan el un led
HIGH = 0x73
LOW = 0x63

#Se establece la direccion del Arduino
arduino = 0x04
#Se establece un objeto correspondiente al canal SMBUS 1
i2c = SMBus(1)

if len(sys.argv) > 1:
	if sys.argv[1] == '1':
		i2c.write_byte(arduino,HIGH)
	elif sys.argv[1] == '0':
		i2c.write_byte(arduino,LOW)
