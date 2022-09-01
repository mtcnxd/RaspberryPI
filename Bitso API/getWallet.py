#!/usr/bin/python

import time
import hmac
import hashlib
import requests
import json

bitso_key = "BLpkbWFduP"
bitso_secret = "34cfc69a8845fbe7832a8845895c956a"
http_method = "GET" # Change to POST if endpoint requires data
request_path = "/v3/balance/"
parameters = {}     # Needed for POST endpoints requiring data

# Create signature
nonce =  str(int(round(time.time() * 1000)) + int(round(time.time() * 1000)))
message = nonce+http_method+request_path
signature = hmac.new(bitso_secret.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()

# Build the auth header
auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)
response = requests.get("https://api.bitso.com" + request_path, headers={"Authorization": auth_header})

# Serialize data request
json_str = response.content
json_payload = json.loads(json_str)
json_currency = json.loads(json.dumps(json_payload["payload"]["balances"]))

# Start methods here
def getPriceOf(currency):
    request_path = "https://api.bitso.com/v3/ticker/?book="+currency
    response = requests.get(request_path)
    json_dict = json.loads(response.content)
    json_payload = json_dict['payload']
    return float(json_payload["last"])

# Main code start here
while(True):
    wallet = 0;
    for i in json_currency:
        amount = float(i["total"])
         
        if ( amount > 0 and i["currency"] != "mxn"):       
            value = getPriceOf(i["currency"]+"_mxn") * amount
            wallet = wallet + value
            print(i["currency"] + " \t {:,.4f}".format(amount) + " \t ${:,.2f}".format(value))
        elif (i["currency"] == "mxn"):
            print("mxn \t\t\t ${:,.2f}".format(amount))
            wallet = wallet + amount
    
    print("-----------------------------------")        
    print("Total wallet value is: \t ${:,.2f} ".format(wallet))
    print("-----------------------------------")
    time.sleep(60)
