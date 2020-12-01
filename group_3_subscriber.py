# group_3_subscriber.py
import paho.mqtt.client as mqtt
import group_3_util as util
import json

def on_message(client, userdata, message):
 data = message.payload.decode('utf-8')
 obj = json.loads(data)
 util.print_data(obj)


client = mqtt.Client()
client.on_message = on_message
client.connect('localhost', 1883)
client.subscribe('GROUP3')

while True:
 client.loop_forever()