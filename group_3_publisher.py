#group_3_publisher.py
import group_3_util as util
import paho.mqtt.client as mqtt
import json
import time
import random

#print(json.dumps(data))

def shouldSend() -> bool:
    # value = random.randint(0, 99)
    # print(value)
    # if (value == 22 or value == 77):
    #     return False
    # return True
    value = random.randint(0, 10)
    print(value)
    if (value == 2 or value == 7):
        return False
    return True

client = mqtt.Client()
client.connect('localhost', 1883)
client.loop_start()

while True:
    data = util.create_data()
    if (shouldSend()):
        client.publish('GROUP3', json.dumps(data))
        print('Message sent')
    else:
        print('All good! No message send')
    time.sleep(5)
client.loop_stop()
# util.print_data(data)
# Util.start_id = 122
# data = Util.create_data()
# Util.print_data(data)
