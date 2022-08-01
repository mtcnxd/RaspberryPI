#!/usr/bin/python
import requests
import json
import time

username = "mtcnxd"
key = "f0dd74b723d90a2ca81a2fc6af57c5e0dc6982e4"

def getResponse():
    request_path = "/api/v2/mtcnxd/feeds/temperature/data?x-aio-key="+key
    response = requests.get("https://io.adafruit.com" + request_path)
    json_dict = json.loads(response.content)
    json_payload = json_dict[0]
    created = json_payload['created_at']
    value = json_payload['value']
    print "Time: " + created + " Temperature: " + value
    
def getRequest():
    request_path = "/api/groups/my-feeds/send.json?x-aio-key="+key+"&eco=0"
    response = requests.post("http://io.adafruit.com" + request_path);
    print "OK: " + str(response)
    

#getResponse()
getRequest()