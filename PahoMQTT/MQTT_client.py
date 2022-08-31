from paho.mqtt import client as mqtt_client
import random
import time

broker = 'io.adafruit.com'
port = 1883
topic = "mtcnxd/feeds/temperature"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'mtcnxd'
password = 'f0dd74b723d90a2ca81a2fc6af57c5e0dc6982e4'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1    


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)    
    subscribe(client)
    client.loop_forever()


run()