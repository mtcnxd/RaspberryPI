#! /bin/bash

#Enciende
#i2cset -y 1 0x04 0x73
i2cset -y 1 0x04 1

#Apaga
#i2cset -y 1 0x04 0x63