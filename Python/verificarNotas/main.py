#!/usr/bin/python
import json
import urllib
import urllib2
import time
import imaplib
import smtplib

# Definicion de funciones
        
def sendMarcosSMS(value1):
    print "SEND MARCOS SMS"
    ifttt = "https://maker.ifttt.com/trigger/verificarNotas/with/key/b02sH9pYZV0xykH4H8K2wT"
    data = json.dumps({"value1": value1})
    req = urllib2.Request(ifttt, data, {'Content-Type': 'application/json'})
    response = urllib2.urlopen(req)     

# Envia un correo a un destinatario usando una cuenta de Gmail
def sendMail(mensaje):
    imap_host = 'imap.gmail.com'
    imap_user = 'mtc.nxd@gmail.com'
    imap_pass = 'tucm1985'
    imap_server = 'smtp.gmail.com:587'

    destinatarios = ["mtc.nxd@gmail.com","soporte@santoslugo.com.mx"]

    try :
        smtp = smtplib.SMTP(imap_server)
        smtp.starttls()
        smtp.login(imap_user, imap_pass)
        smtp.sendmail(imap_user, destinatarios ,mensaje)
        smtp.quit()
    except :
        print "ERROR AL ENVIAR CORREO!"

# Inicio del programa principal
# Los datos recibidos son los mismos que el main activity Android

maxNumNotas = 30
total = 0

url = "http://www.santoslugo.com.mx/verificarNotas.php"
jsonString = urllib2.urlopen(url)
jsonObject = json.load(jsonString)

size = len(jsonObject)

for i in range (0,size):    
    total = total + jsonObject[i]["Notas"]
    if jsonObject[i]["Notas"] > maxNumNotas:
        print "----------------------------------------"
        print "ENVIANDO ALERTA ..."
        sendMail("SE HAN ACUMULADO MAS DE " + str(total) + " NOTAS DE LA SUCURSAL " + jsonObject[i]["Sucursal"])
        #sendMarcosSMS(total)
        #sendAngelSMS(total)
    

print "----------------------------------------"
print "NOTAS PENDIENTES POR SINCRONIZAR: " + str(total)
print "----------------------------------------"

time.sleep(2)
