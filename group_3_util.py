#Lab13
#group_3_util.py
import random
import time
import json
import group_3_data_generator as data_generator

# To Run/Test
# Open 2 Terminals
# Run group_3_subscriber.py
# Run group_3_publisher.py


# class PythonUtil:
#     id = 110
#     _ID = 111
#     def __init__(self):
#         self.id = self._ID 
#         self.__class__._ID += 1

#     @staticmethod
#     def create_data():
#         self.id = self._ID 
#         self.__class__._ID += 1
#         user = {
#             "login": "giangkw13",
#             "id": self.id,
#             "node_id": "MDQ6VXNlcjI=",
#             "type": "User",
#             "site_admin": 'false',
#             "name": "Giang Nguyen",
#             "company": "St. Michael's Hospital",
#             "location": "2 Queen Street",
#             "email": "giangkawaii1999@gmail.com",
#             "bio": "Sample user for project",
#             "stats": {
#                 "public_repos": int(random.gauss(80, 1)),
#                 "followers": int(random.gauss(20000,350)),
#                 "following": int(random.gauss(200, 12)),
#             },
#             "status": "Active",
#             "retrieve_at": time.asctime()
#             #"created_at": "",
#             #"updated_at": ""
#         }
#         return user

#     @staticmethod
#     def print_data(json_obj):
#         #json_obj = json.loads(json_obj)
#         print(f'UID#         {json_obj["id"]}')
#         print(f'Username:    {json_obj["login"]}')
#         print(f'Email:       {json_obj["email"]}')
#         print(f'Bio:         {json_obj["bio"]}')
#         print(f'Public repo: {json_obj["stats"]["public_repos"]}')
#         print(f'Following:   {json_obj["stats"]["following"]}')
#         print(f'Followers:   {json_obj["stats"]["followers"]}')
#         print(f'Active:      {json_obj["status"]}')
#         print(f'Retrieve at: {json_obj["retrieve_at"]}')

start_id = 111

def create_data():
    data = data_generator.Simulator(37,0.5)
    user = {
        "login": "giangkw13",
        "id": start_id,
        "node_id": "MDQ6VXNlcjI=",
        "type": "User",
        "site_admin": 'false',
        "name": "Giang Nguyen",
        "company": "St. Michael's Hospital",
        "location": "2 Queen Street",
        "email": "giangkawaii1999@gmail.com",
        "bio": "Sample user for project",
        "body_temp": data.generator_1(),
        "stats": {
            "public_repos": int(random.gauss(80, 1)),
            "followers": int(random.gauss(20000,350)),
            "following": int(random.gauss(200, 12)),
        },
        "status": "Active",
        "retrieve_at": time.asctime()
        #"created_at": "",
        #"updated_at": ""
    }
    #start_id+=1
    return user

def print_data(json_obj):
    print('---------------------------------------------------')
    print(f'UID#         {json_obj["id"]}')
    print(f'Username:    {json_obj["login"]}')
    print(f'Email:       {json_obj["email"]}')
    print(f'Bio:         {json_obj["bio"]}')
    print(f'Body Temp:   {json_obj["body_temp"]:.1f}*C')
    print(f'Public repo: {json_obj["stats"]["public_repos"]}')
    print(f'Following:   {json_obj["stats"]["following"]}')
    print(f'Followers:   {json_obj["stats"]["followers"]}')
    print(f'Active:      {json_obj["status"]}')
    print(f'Retrieve at: {json_obj["retrieve_at"]}')





