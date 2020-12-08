#group_3_util_proj.py
import random
import time
import json
import group_3_data_generator as data_generator

# To Run/Test
# Open 2 Terminals
# Run group_3_subscriber.py
# Run group_3_publisher.py

def create_data():
    data = data_generator.Simulator(37,0.5)
    json = {
        "body_temp": data.generator_1(),
        "retrieve_at": time.asctime()
    }
    return json

def create_data_wild_data():
    data = data_generator.Simulator(99,10)
    json = {
        "body_temp": data.generator_1(),
        "retrieve_at": time.asctime()
    }
    return json

def print_data(json_obj):
    print('---------------------------------------------------')
    print(f'Body Temp:   {json_obj["body_temp"]:.1f}*C')
    print(f'Retrieve at: {json_obj["retrieve_at"]}')