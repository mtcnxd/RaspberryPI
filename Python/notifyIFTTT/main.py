#!/usr/bin/python
import json
import urllib
import urllib2
import time
import imaplib
import smtplib
        
def sendIFTTT(value1):
    print "SEND IFTTT"
    urlInsert = "https://maker.ifttt.com/trigger/verificarNotas/with/key/b02sH9pYZV0xykH4H8K2wT"
    data = json.dumps({"value1": value1})
    req = urllib2.Request(urlInsert, data, {'Content-Type': 'application/json'})
    response = urllib2.urlopen(req)    


sendIFTTT(20)