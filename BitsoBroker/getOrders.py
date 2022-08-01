#!/usr/bin/python

import time
import hmac
import hashlib
import requests
import json

bitso_key = "BLpkbWFduP"
bitso_secret = "34cfc69a8845fbe7832a8845895c956a"
http_method = "GET" # Change to POST if endpoint requires data
request_path = "/v3/open_orders/"
parameters = {}     # Needed for POST endpoints requiring data

# Create signature
nonce =  str(int(round(time.time() * 1000)) + int(round(time.time() * 1000)))
message = nonce+http_method+request_path
signature = hmac.new(bitso_secret.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()

# Build the auth header
auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)
    
# Send request
if (http_method == "GET"):
    response = requests.get("https://api.bitso.com" + request_path, headers={"Authorization": auth_header})

# Serialize data request
json_dict = json.loads(response.content)
json_payload = json_dict['payload']
json_length = len(json_payload)

# Show orders and moves
for i in range(json_length):
    print str(i+1)+") "+ json_payload[i]["side"] +" | "+ json_payload[i]["book"] +" | "+ json_payload[i]["original_amount"] +" | "+ json_payload[i]["price"]
