import json
import requests
import time
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()

def getBitsoStatistics():
	url = "http://test.fortech.mx/wservice/api.php"
	data = { 'request':'statistics', 'userid':1 }

	response = requests.post(url, data)
	jsonObject = json.loads(response.text)	
	return jsonObject


while True:
	data = getBitsoStatistics()

	for row in data:
		print ( row )

		firstLine  = row['key']
		secondLine = row['value']

		mylcd.lcd_clear()
		mylcd.lcd_display_string(firstLine , 1, 0)
		mylcd.lcd_display_string(secondLine, 2,0)
		time.sleep(5)
