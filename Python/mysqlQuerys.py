#! /usr/bin/python

import MySQLdb as mysql
import time

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
        
def mysqlInsert():
    try:
        connection = mysql.connect ('localhost', 'root', 'nodoubt', 'homeControl')
        with connection:
            cursor = connection.cursor()
            cursor.execute("insert into devices (nameDevice, statusDevice, valueDevice) values('Secundarias', 42, 84);")

    except mysql.Error, e:
        print "Error"
        sys.exit(1)


print "Insertando a base de datos"
print "-------------------------------"
mysqlInsert()

time.sleep(1)

print "Consultando base de datos"
print "-------------------------------"
mysqlSelect()