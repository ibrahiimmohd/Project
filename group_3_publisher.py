#group_3_publisher.py
import group_3_util as util
import paho.mqtt.client as mqtt
import json

data = util.create_data()
#print(json.dumps(data))

client = mqtt.Client()
client.connect('localhost', 1883)
client.loop_start()
client.publish('GROUP3', json.dumps(data))
print('Message sent')
client.loop_stop()
# util.print_data(data)
# Util.start_id = 122
# data = Util.create_data()
# Util.print_data(data)
