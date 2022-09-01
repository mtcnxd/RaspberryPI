#!/usr/bin/python

import time
import hmac
import hashlib
import requests
import json

def getPriceOf(currency):
    request_path = "https://api.bitso.com/v3/ticker/?book="+currency
    response = requests.get(request_path)
    json_dict = json.loads(response.content)
    json_payload = json_dict['payload']
    return float(json_payload["last"])

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
    
# Send request
response = requests.get("https://api.bitso.com" + request_path, headers={"Authorization": auth_header})

# Serialize data request
json_str = response.content
json_payload = json.loads(json_str)
json_currency = json.loads(json.dumps(json_payload["payload"]["balances"]))

# Show balances and currency
for i in json_currency:
    total = float(i["total"])
     
    if ( total > 0 and i["currency"] != "mxn"):       
        price = getPriceOf(i["currency"]+"_mxn") * total
        print(i["currency"] + " - {:.3f}".format(total) + " - " + str(price))
        
        
        