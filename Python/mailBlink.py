#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import imaplib

imap_host = 'imap.gmail.com'
imap_user = 'mtc.nxd@gmail.com'
imap_pass = 'tucm1985'
imap_server = 'smtp.gmail.com:587'

ledPin = 14
haveMail = False
counter = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

# Realiza un parpadeo del LED
def blink():   
    for i in range(5):
        GPIO.output(ledPin, True)
        time.sleep(0.5)
        GPIO.output(ledPin, False)
        time.sleep(0.5)
        
# Verifica si hay correos nuevos en la bandeja de entrada de Gmail
def checkMail():  
    imap = imaplib.IMAP4_SSL(imap_host)
    imap.login(imap_user, imap_pass)

    folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")
    NotRead = int(UnseenInfo[0].split()[2].strip(').,]'))

    return NotRead        

# Ciclo infinito para la verificacion del correo
while True:
    print "Verificando bandeja de entrada..."
    print "---------------------------------"    
    newMail = checkMail()
    
    if newMail == 1:
        print "Tienes ",newMail, " correo sin leer"
	
	if newMail > 1:
	    print "Tienes ",newMail, " correos sin leer"
        haveMail = True
        
    else:
        haveMail = False
        
    while (haveMail == True):
        blink()
        print "---------------------------------"
        print "Alerta correo nuevo"
        time.sleep (1)
        counter = counter + 1
        
        if counter >= 3:
            counter = 0
            break;

    time.sleep (10)
