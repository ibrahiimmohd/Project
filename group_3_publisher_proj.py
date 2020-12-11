# group_3_publisher_proj.py
import group_3_util_proj as util
import paho.mqtt.client as mqtt
import json
import time
import random
import group_3_data_generator as generator

PUBLISH_TOPIC = 'GROUP3'

def shouldSend() -> bool:
    value = random.randint(0, 99)
    if (value == 22 or value == 77):
        return False
    return True



client = mqtt.Client()
client.connect('localhost', 1883)
client.loop_start()

while True:
    # Replica publisher sending decision
    if (shouldSend()):
        value = random.randint(0, 99)
        # Replica corrupted data
        if (value == 12 or value == 45):
            corrupted_data = {
                "error_message":"#500.! Internal Server Error",
                "retrieve_at": time.asctime()
            }
            client.publish(PUBLISH_TOPIC, json.dumps(corrupted_data))
            print('Message sent.! Corrupted Data')
        elif ((value > 96)):
            data = util.create_data_wild_data()
            client.publish(PUBLISH_TOPIC, json.dumps(data))
            print('Message sent.! Wild data')
        else:
            data = util.create_data()
            client.publish(PUBLISH_TOPIC, json.dumps(data))
            print('Message sent')
    else:
        print('All good! No message send')
    
    # Replica publisher iteration
    time.sleep(10)
client.loop_stop()