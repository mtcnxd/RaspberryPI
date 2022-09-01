#!/usr/bin/python
import requests
import json
import time

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
     

while (True):
    weather = getWeather()    
    
    print "Temperature: " + weather['temperature']
    print "Humidity: " + weather['humidity'] + "%"    
    print "Wind Speed: " + weather['wind'] + " m/s"
    print "Degrees: " + weather['degrees']    
    print "Clouds: " + weather['clouds']
    print "-----------------------------------"
    
    time.sleep(10)
    