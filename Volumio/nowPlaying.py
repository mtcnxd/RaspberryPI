import requests
import json
import time
import I2C_LCD_driver
from datetime import datetime

mylcd = I2C_LCD_driver.lcd()
url = "http://localhost:3000/api/v1/getState"


def getWeather():
    weather = {}    
    city = "merida"
    api_key = "192dbed2ac66d17d5f75780635e474fa"
    request_path = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
    
    response = requests.get(request_path)
    json_dict = json.loads(response.content)
    
    json_payload = json_dict['main']
    current_temp = float(json_payload['temp']) - 273.15
    current_humidity = json_payload['humidity']
     
    weather['temperature'] = str(current_temp)
    weather['humidity'] = str(current_humidity)
        
    json_payload = json_dict['wind']     
    wind_speed = json_payload['speed']
    degrees = json_payload['deg']
    
    weather['wind'] = str(wind_speed)
    weather['degrees'] = str(degrees)    
    
    json_payload = json_dict['clouds']     
    clouds_all = json_payload['all']
    
    weather['clouds'] = str(clouds_all)
    return weather


mylcd.backlight(0)
temp = False

# PROGRAM START HERE

while True:
	now = datetime.now()
	weather = getWeather()
	response = requests.request("GET", url)
	jsonText = json.loads(response.text)

	if jsonText['status'] == 'pause':
		if temp == True:
			firstLine  = "TEMP " + weather['temperature']
			secondLine = "HUMI " + weather['humidity'] + "%"
			temp = False

		else:
			firstLine  = "TIME " + str(now.hour) + ":" + str(now.minute) +":"+ str(now.second)
			secondLine = "DATE " + str(now.day) + "/" + str(now.month) +"/"+ str(now.year)
			temp = True

		mylcd.lcd_clear()
		mylcd.lcd_display_string(firstLine , 1, 0)
		mylcd.lcd_display_string(secondLine, 2,0)

	else:

		artist = jsonText['artist']
		title  = jsonText['title']
		album  = jsonText['album']
		
		#mylcd.scroll_Display_Left()
		#mylcd.lcd_display_string(artist + " " + title , 1, 0)
		#mylcd.lcd_display_string(album, 2,0)


	time.sleep(2)