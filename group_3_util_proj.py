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
    user = {
        "body_temp": data.generator_1(),
        "retrieve_at": time.asctime()
    }
    return user

def print_data(json_obj):
    print('---------------------------------------------------')
    print(f'Body Temp:   {json_obj["body_temp"]:.1f}*C')
    print(f'Retrieve at: {json_obj["retrieve_at"]}')