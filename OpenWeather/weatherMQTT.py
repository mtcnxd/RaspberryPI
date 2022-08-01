#!/usr/bin/python
import requests
import json
import time
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print("Payload: " + str(msg.payload))
    
client = mqtt.Client()
client.on_message = on_message

client.username_pw_set("mtcnxd", "f0dd74b723d90a2ca81a2fc6af57c5e0dc6982e4")
client.connect("io.adafruit.com", 1883, 60)

client.subscribe("mtcnxd/feeds/led")
client.loop_start()    

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
    client.publish("mtcnxd/feeds/temperature", weather['temperature'])
    client.publish("mtcnxd/feeds/humidity", weather['humidity'])
    
    time.sleep(300)
    