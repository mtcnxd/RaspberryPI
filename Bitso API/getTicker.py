#!/usr/bin/python

import time
import hmac
import hashlib
import requests
import json

def getPrice():
    request_path = "https://api.bitso.com/v3/ticker/"
    response = requests.get(request_path)
    json_dict = json.loads(response.content)
    json_payload = json_dict['payload']
    json_length = len(json_payload)
    
    for i in range(json_length):
        if 'mxn' in str(json_payload[i]["book"]):
            print "[" + json_payload[i]["book"] + "] \t $ " + json_payload[i]["last"]


def getPriceOf(currency):
    request_path = "https://api.bitso.com/v3/ticker/?book="+currency
    response = requests.get(request_path)
    json_dict = json.loads(response.content)
    json_payload = json_dict['payload']
    print json_payload["last"] + " " + json_payload["book"]
    

getPrice()
#getPriceOf("ltc_mxn")