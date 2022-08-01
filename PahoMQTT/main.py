import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print("Payload: " + str(msg.payload))    

client = mqtt.Client()
client.on_message = on_message
client.connect("mqtt.eclipse.org", 1883, 60)
client.subscribe("/sensors/move")

while True:    
    client.loop_start()
    temperature = 25.5
    #client.publish("/sensors/move", temperature)    
    time.sleep(1)

