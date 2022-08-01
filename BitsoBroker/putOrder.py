#!/usr/bin/python

import time
import hmac
import hashlib
import requests
import json

http_method = "POST"
bitso_key = "BLpkbWFduP"
bitso_secret = "34cfc69a8845fbe7832a8845895c956a"
request_path = "/v3/orders/"
parameters = {"book":"mana_mxn","side":"sell","type":"limit","major":"10","price":"1.72"}
#parameters = {"book":"bat_mxn","side":"buy","type":"limit","major":"10","price":"4.35"}     
# Needed for POST endpoints requiring data

# Create signature
nonce =  str(int(round(time.time() * 1000)) + int(round(time.time() * 1000)))
print nonce
message = nonce+http_method+request_path
message += json.dumps(parameters)
signature = hmac.new(bitso_secret.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()

# Build the auth header
auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)
    
# Send request
response = requests.post("https://api.bitso.com" + request_path, json = parameters, headers={"Authorization": auth_header})

# Serialize data request
json_str = response.content

print json_str
