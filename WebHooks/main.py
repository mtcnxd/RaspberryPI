#!/usr/bin/python
import json
import urllib
import urllib2
import time

api = "b02sH9pYZV0xykH4H8K2wT"
trigger = "loxone"
        
def sendIFTTT(value):
    urlInsert = "https://maker.ifttt.com/trigger/"+trigger+"/with/key/"+api
    data = json.dumps({"value1": value})
    req = urllib2.request(urlInsert, data, {'Content-Type': 'application/json'})
    response = urllib2.urlopen(req) 


print "send trigger to IFTTT"
sendIFTTT(25)