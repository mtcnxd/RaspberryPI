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

def showFullData(book):
    # Create signature
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
    

def writeFile(data):
    now = datetime.now()
    f = open('prices.txt','a')
    f.write(str(now) + "\t")
    f.write(str(data) + "\n")
    f.close()    


# Main code
last_price = 0

while(True):
    book = "ltc_mxn"
    showFullData(book)
    time.sleep(1)
    current_price = getPriceOf(book)
    writeFile(current_price)

    if (current_price - last_price) != 0:
        diferencia = current_price - last_price
        print "El precio cambio: {:,.2f}".format(diferencia)
        print "----------------------------"
        last_price = current_price
    
    time.sleep(30)
    
