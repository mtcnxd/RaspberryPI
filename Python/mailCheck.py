import imaplib
import smtplib
import json
import urllib2
import email
import email.mime.application

imap_host = 'imap.gmail.com'
imap_user = 'mtc.nxd@gmail.com'
imap_pass = 'tucm1985'
imap_server = 'smtp.gmail.com:587'

# Envia los datos a IFTTT para activar una opcion por webRequest
def sendIFTTT(value1):
    print "Enviando a IFTTT"
    print "---------------------------------"
    urlInsert = "https://maker.ifttt.com/trigger/sensor_pir/with/key/bg8MZhzF-UTNr4WsrU8O3T"
    data = json.dumps({"value1": value1})
    req = urllib2.Request(urlInsert, data, {'Content-Type': 'application/json'})
    response = urllib2.urlopen(req)    

# Verifica si hay correos nuevos en la bandeja de entrada de Gmail
def checkMail():
    print "Verificando bandeja de entrada..."
    print "---------------------------------"    
    imap = imaplib.IMAP4_SSL(imap_host)
    imap.login(imap_user, imap_pass)

    folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")
    NotReadCounter = int(UnseenInfo[0].split()[2].strip(').,]'))

    if NotReadCounter >= 1 :
        if NotReadCounter >= 2:
            print "Tienes ", NotReadCounter," correos nuevos"
        else:
            print "Tienes ", NotReadCounter," correo nuevo"
            
    else :
        print "No tienes correo nuevo"        

# Envia un correo a un destinatario usando una cuenta de Gmail
def sendMail(value):
    print "Enviando correo..."
    print "---------------------------------"    
    mensaje = email.mime.Multipart.MIMEMultipart()
    mensaje['Subject'] = 'Mail send from Raspberry Pi'
    
    body = email.mime.Text.MIMEText( "Hello the value is " + str( value ) )
    mensaje.attach(body)    
    
    filename = '/home/pi/Captures/capture.jpg'
    fOpen = open(filename, 'rb')
    att = email.mime.application.MIMEApplication(fOpen.read(),_subtype="jpg")
    fOpen.close()
    
    att.add_header('Content-Disposition', 'attachment', filename = filename)
    
    mensaje.attach(att)    
    
    try :
        smtp = smtplib.SMTP(imap_server)
        smtp.starttls()
        smtp.login(imap_user, imap_pass)
        smtp.sendmail(imap_user, [imap_user], mensaje.as_string())
        print "Enviado OK"
        smtp.quit()
    except :
        print "Error!"

checkMail()
#sendMail(35)
#sendIFTTT("HolaMundo")
