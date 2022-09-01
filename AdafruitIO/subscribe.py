import sys
import time
from Adafruit_IO import MQTTClient

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'f0dd74b723d90a2ca81a2fc6af57c5e0dc6982e4'
ADAFRUIT_IO_USERNAME = 'mtcnxd'

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'temperature'


# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
    client.subscribe(FEED_ID)

def subscribe(client, userdata, mid, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print('Subscribed to {0} with QoS {1}'.format(FEED_ID, granted_qos[0]))

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribe

client.connect()

# client.publish('temperature', 'Connected')

# Start a message loop that blocks forever waiting for MQTT messages to be
# received.  Note there are other options for running the event loop like doing
# so in a background thread--see the mqtt_client.py example to learn more.

# client.loop_blocking()

# The first option is to run a thread in the background so you can continue
# doing things in your program.

client.loop_background()

# Now send new values every 10 seconds.

print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
while True:
    value = 13
    print('Publishing {0} to temperature.'.format(value))
    client.publish('temperature', value)
    time.sleep(10)