#!/usr/bin/python
import json
import urllib
import urllib2
import httplib
import time
import imaplib
import smtplib

imap_host = 'imap.gmail.com'
imap_user = 'mtc.nxd@gmail.com'
imap_pass = 'tucm1985'
imap_server = 'smtp.gmail.com:587'

#Realiza una consulta de los datos del main activity Android

send = 0

# Envia una consulta a MySQL a traves de POST y devuelve los datos en JSON
def sendPost():
    urlServer = "http://remotehomecontrol.esy.es/service/getPost.php"
    query = urllib.urlencode({"query":"SELECT * FROM ifttt ORDER BY idData DESC LIMIT 1"})
    response = urllib2.urlopen(urlServer, query)
    jsonString = response.read()
    jsonObject = json.loads(jsonString)[0]
    temp = jsonObject['value2']
    clouds = jsonObject['value1']
    return temp, clouds

# Envia un correo a un destinatario usando una cuenta de Gmail
def sendMail(mensaje):
    print "----------------------------------------"
    
    try :
        smtp = smtplib.SMTP(imap_server)
        smtp.starttls()
        smtp.login(imap_user, imap_pass)
        smtp.sendmail(imap_user, imap_user, mensaje)
        print "OK"
        smtp.quit()
    except :
        print "Error!"

    print "----------------------------------------"

while True:
    temp = float( sendPost()[0] )
    clouds = sendPost()[1]

    if temp >= 25.00:
        print "It's getting warmer, actualmente son ", temp, " grados, clouds ", clouds
        print "----------------------------------------"
        
        if send == 0:
            print "Sending data..."
            sendMail("It's getting warmer")
            send = 1
            
    else :
        print "It's getting colder, actualmente son ", temp, " grados, clouds ", clouds
        print "----------------------------------------"
        if send == 1:
            print "Sending data..."
            sendMail("It's getting colder")
            send = 0
        
    time.sleep(30)
