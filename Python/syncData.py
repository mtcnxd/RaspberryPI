#! /usr/bin/python

import MySQLdb as mysql
import time
import json
import urllib
import urllib2

# Realiza una consulta a la base de datos interna a la raspberry
def mysqlSelect():
    try:
        connection = mysql.connect ('localhost', 'root', 'nodoubt', 'homeControl')
        with connection:
            cursor = connection.cursor()
            cursor.execute("select * from devices;")
            rows = cursor.fetchall()
            for row in rows:
                print row[0],"\t | ", row[1]," \t ", row[2]," \t ", row[3]

    except mysql.Error, e:
        print "Error"
        sys.exit(1)

# Inserta los datos obtenidos del servidor para actualizar la base de datos
def mysqlInsert(name, status, value):  
    try:
        connection = mysql.connect ('localhost', 'root', 'nodoubt', 'homeControl')
        with connection:
            cursor = connection.cursor()
            cursor.execute("insert into devices (nameDevice, statusDevice, valueDevice) values ('" + name + "', '" + status + "', '" + value + "')")

    except mysql.Error, e:
        print "Error"
        sys.exit(1)

# Realiza una consulta establecida en el archivo main.php  

def selectJson():
    urlSelect = "http://remotehomecontrol.esy.es/service/main.php"
    jsonString = urllib2.urlopen(urlSelect)
    jsonObject = json.load(jsonString)
    return jsonObject


# Inicio del codigo principal

print "Descargando datos del servidor remoto..."
print "----------------------------------------"
jsonData = selectJson()
time.sleep(1)

print "Actualizando datos del servidor local..."
print "----------------------------------------"

name = str( jsonData[0]["nameLight"] )
status = str( jsonData[0]["stateLight"])
value = str( jsonData[3]["value1"] )

mysqlInsert( name , status, value)
time.sleep(1)

print "Datos actualizados correctamente"
print "----------------------------------------"
mysqlSelect()

print "Luces: " + str( jsonData[0]["nameLight"] ) + " State: " + str( jsonData[0]["stateLight"])
print "Luces: " + str( jsonData[1]["nameLight"] ) + " State: " + str( jsonData[1]["stateLight"])
print "Luces: " + str( jsonData[2]["nameLight"] ) + " State: " + str( jsonData[2]["stateLight"])
print "----------------------------------------"
print "Nubes: " + str( jsonData[3]["value1"] )
print "Temp: " + str( jsonData[3]["value2"] )
print "Time: " + str( jsonData[3]["value3"] )
print "----------------------------------------"
