import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print("Payload: " + str(msg.payload))    

client = mqtt.Client()
client.on_message = on_message

client.username_pw_set("mtcnxd", "f0dd74b723d90a2ca81a2fc6af57c5e0dc6982e4")
client.connect("io.adafruit.com", 1883, 60)

client.subscribe("mtcnxd/feeds/led")
client.loop_start()

counter = 0;

while True:
    client.publish("mtcnxd/feeds/sensor", counter)
    counter = counter + 1
    time.sleep(5)

