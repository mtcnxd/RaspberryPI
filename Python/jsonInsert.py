#!/usr/bin/python
import json
import urllib
import urllib2

#Realiza una consulta especifica en el archivo query PHP
def jsonSelect():
    urlSelect = "http://remotehomecontrol.esy.es/service/query.php"
    jsonString = urllib2.urlopen(urlSelect)
    jsonObject = json.load(jsonString)[0]

    print jsonObject
    print "------------------------------"
    print "Value1: " + jsonObject['value1']
    print "Value2: " + jsonObject['value2']
    print "Value3: " + jsonObject['value3']


#Inserta los datos en el servidor con valores establecidos
def jsonInser():
    print "------------------------------"
    print "Enviando datos al servidor"
    
    urlInsert = "http://remotehomecontrol.esy.es/service/ifttt.php"
    data = json.dumps({"value1": "Javier", "value2":"Perez", "value3":"Ortiz"})
    req = urllib2.Request(urlInsert, data, {'Content-Type': 'application/json'})
    response = urllib2.urlopen(req)
    #print response.read()
    
jsonInsert()
