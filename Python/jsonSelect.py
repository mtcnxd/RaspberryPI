#!/usr/bin/python
import json
import urllib
import urllib2

# Realiza una consulta establecida en el archivo main.php  
# los datos recibidos son similares al main activity Android

urlSelect = "http://remotehomecontrol.esy.es/service/main.php"
jsonString = urllib2.urlopen(urlSelect)
jsonObject = json.load(jsonString)

#print json.dumps(jsonObject, indent=2)
print "----------------------------------------"
print "Luces: " + str( jsonObject[0]["nameLight"] ) + " State: " + str( jsonObject[0]["stateLight"])
print "Luces: " + str( jsonObject[1]["nameLight"] ) + " State: " + str( jsonObject[1]["stateLight"])
print "Luces: " + str( jsonObject[2]["nameLight"] ) + " State: " + str( jsonObject[2]["stateLight"])
print "----------------------------------------"
print "Nubes: " + str( jsonObject[3]["value1"] )
print "Temp: " + str( jsonObject[3]["value2"] )
print "Time: " + str( jsonObject[3]["value3"] )
print "----------------------------------------"