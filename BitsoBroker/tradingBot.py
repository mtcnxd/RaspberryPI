#!/usr/bin/python

import time
import hmac
import hashlib
import requests
import json
from datetime import datetime

bitso_key = "BLpkbWFduP"
bitso_secret = "34cfc69a8845fbe7832a8845895c956a"
http_method = "GET" # 
request_path = "/v3/balance/"

# Create functions
def getPriceOf(book):
    request_path = "https://api.bitso.com/v3/ticker/?book="+book
    response = requests.get(request_path)
    json_dict = json.loads(response.content)
    json_payload = json_dict['payload']
    return float(json_payload["last"])

def getBalances(book):
    nonce =  str(int(round(time.time() * 1000)) + int(round(time.time() * 1000)))
    message = nonce+http_method+request_path
    signature = hmac.new(bitso_secret.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()
    auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)
    response = requests.get("https://api.bitso.com" + request_path, headers={"Authorization": auth_header})
    
    # Serialize data request
    json_str = response.content
    json_payload = json.loads(json_str)
    json_currency = json.loads(json.dumps(json_payload["payload"]["balances"]))
    
    available = float(json_currency[1]["available"])
    price = getPriceOf(book)
    convert = round(available * price, 2)
    
    print "Currency: " + json_currency[6]["currency"]
    print "Locked: " + json_currency[6]["locked"]
    print "Available: " + json_currency[6]["available"]
    print "Price: $ {:,.2f}".format(price)
    print "----------------------------"
    

def writeFile(price, porcent):
    now = datetime.now()
    f = open('values.txt','a')
    f.write(str(now) + "\t")
    f.write("$" + str(price) + "\t")
    f.write(str(porcent) + "%\n")
    f.close()
    
username = "mtcnxd"
key = "f0dd74b723d90a2ca81a2fc6af57c5e0dc6982e4"

def getRequest(value):
    request_path = "/api/groups/cryptocurrencys/send.json?x-aio-key="+key+"&xrp_mxn="+str(value)
    response = requests.post("http://io.adafruit.com" + request_path);


# Main code starts here
last_price = 0

while(True):
    book = "xrp_mxn"
    delay = 90
    change = 0.6
    current_price = getPriceOf(book)

    print "Current date: " + datetime.now().strftime("%d/%m/%Y")        
    print "Current time: " + datetime.now().strftime("%I:%M:%S %p")    
    print "Price " + book + ": ${:,.2f}".format(current_price)

    if (current_price - last_price) != 0:
        diferencia = current_price - last_price
        porcent = (diferencia/current_price) * 100
        last_price = current_price
        writeFile(current_price, porcent)
        getRequest(current_price)
        
        print "Price change to: {:,.2f}".format(diferencia)
        print "Percent change is: {:.2f}%".format(porcent)
        print "-----------------------------"
        
        #if ((porcent < (change * -1)) or (porcent > change)):
                    
    time.sleep(delay)
    