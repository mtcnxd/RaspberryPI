import json
import urllib
import urllib2
import time
import pyowm

# Realiza la consulta de los datos del clima en OpenWeatherMap
def checkWeather():
    apikey = "c8fddc03a83fcd5ef83738a8f32e5b9e"
    owm = pyowm.OWM(apikey)
    print "Conectanto con openWeatherMap"
    print "--------------------------------"
    observation = owm.weather_at_place('Merida,MX')
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    nuves = w.get_status()
    return nuves, temp

# Envia los datos a una base de datos por medio de JSON
def sendServer(value1, value2, value3):
    print "Enviando datos a servidor remoto"
    print "--------------------------------"    
    urlInsert = "http://remotehomecontrol.esy.es/service/ifttt.php"
    data = json.dumps({"value1": value1, "value2": value2, "value3": value3 })
    req = urllib2.Request(urlInsert, data, {'Content-Type': 'application/json'})
    response = urllib2.urlopen(req)

time.sleep(0.5)
data = checkWeather()
timeStamp = time.strftime("%H:%M:%S - %d/%m/%y")

sendServer(data[0], data[1], timeStamp)