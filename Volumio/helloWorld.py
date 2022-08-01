# Driver LCD
# git clone https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
# Activar i2c desde raspi-conf

import I2C_LCD_driver
import time
import json

mylcd = I2C_LCD_driver.lcd()

while True:
	mylcd.lcd_display_string('Hola Mundo', 1,0)

	time.sleep(1)