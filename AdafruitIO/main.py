from Adafruit_IO import Client, Feed, Data, RequestError

ADAFRUIT_IO_KEY = 'f0dd74b723d90a2ca81a2fc6af57c5e0dc6982e4'
ADAFRUIT_IO_USERNAME = 'mtcnxd'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    temperature = aio.feeds('temperature')
except RequestError:
    feed = Feed(name="temperature")
    temperature = aio.create_feed(feed)
    

data = aio.data('temperature')

count = 1
for d in data:
    print(str(count) + " Time: " + d.created_at + " Temperature: " + d.value)
    count = count + 1
    

data = aio.receive(temperature.key)
print('---------------------------------------')
print('Latest value from temperature: {0}'.format(data.value))    