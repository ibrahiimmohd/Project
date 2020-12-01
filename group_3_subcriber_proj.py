# group_3_subcriber_proj.py
import paho.mqtt.client as mqtt
import group_3_util as util
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Checkbutton
from tkinter.ttk import Combobox

def on_message(client, userdata, message):
 data = message.payload.decode('utf-8')
 obj = json.loads(data)
 uid_var.set(obj["id"])
 username_var.set(obj["login"])
 email_var.set(obj["email"])
 bio_var.set(obj["bio"])
 body_temp_var.set(f'{obj["body_temp"]:.1f}*C')
 public_repo_var.set(obj["stats"]["public_repos"])
 followers_var.set(obj["stats"]["following"])
 following_var.set(obj["stats"]["followers"])
 active_var.set(obj["status"])
 retrieve_at_var.set(obj["retrieve_at"])
 util.print_data(obj)

root = Tk()                                #similar to a windows form 
root.title("Group 3 Final project")       #title of the window
#root.mainloop()

frame = ttk.Frame(                         #create a Frame (container in this case)
  root,                                    #parent of this widget
  width=120,                               #width
  height=80)                              #height

frame.grid()                               #row=0, column=0

frame['padding'] = (5,10)                  #padding
frame['borderwidth'] = 10                  #border
frame['relief'] = 'sunken' 

default_value = "Waiting live data..."

#row 0
uid_label = ttk.Label(           
  frame,                           
  text='User ID:'
  ).grid(
  column=0,                          
  row=0,                            
  sticky=(W, E)) 

uid_var = StringVar()
uid_var.set(default_value)

uid = ttk.Label(           
  frame,                           
  textvariable=uid_var
  ).grid(
  column=1,                          
  row=0,                            
  sticky=(W, E))                      

#row 1
username_label = ttk.Label(           
  frame,                           
  text='Full name:'
  ).grid(
  column=0,                          
  row=1,                            
  sticky=(W, E))                      

username_var = StringVar()
username_var.set(default_value)

username = ttk.Label(           
  frame,
  textvariable = username_var                           
  ).grid(
  column=1,                          
  row=1,                            
  sticky=(W, E))

#row 2
email_label = ttk.Label(           
  frame,                           
  text='Full name:'
  ).grid(
  column=0,                          
  row=2,                            
  sticky=(W, E))                      

email_var = StringVar()
email_var.set(default_value)

email = ttk.Label(           
  frame,
  textvariable = email_var                           
  ).grid(
  column=1,                          
  row=2,                            
  sticky=(W, E))

#row 3
bio_label = ttk.Label(           
  frame,                           
  text='Biography:'
  ).grid(
  column=0,                          
  row=3,                            
  sticky=(W, E))                      

bio_var = StringVar()
bio_var.set(default_value)

bio = ttk.Label(           
  frame,
  textvariable = bio_var                           
  ).grid(
  column=1,                          
  row=3,                            
  sticky=(W, E))

#row 4
body_temp_label = ttk.Label(           
  frame,                           
  text='Body Temp:'
  ).grid(
  column=0,                          
  row=4,                            
  sticky=(W, E))                      

body_temp_var = StringVar()
body_temp_var.set(default_value)

body_temp = ttk.Label(           
  frame,
  textvariable = body_temp_var                           
  ).grid(
  column=1,                          
  row=4,                            
  sticky=(W, E))

#row 5
public_repo_label = ttk.Label(           
  frame,                           
  text='Public repo:'
  ).grid(
  column=0,                          
  row=5,                            
  sticky=(W, E))                      

public_repo_var = StringVar()
public_repo_var.set(default_value)

public_repo = ttk.Label(           
  frame,
  textvariable = public_repo_var                           
  ).grid(
  column=1,                          
  row=5,                            
  sticky=(W, E))

#row 6
following_label = ttk.Label(           
  frame,                           
  text='Following:'
  ).grid(
  column=0,                          
  row=6,                            
  sticky=(W, E))                      

following_var = StringVar()
following_var.set(default_value)

following = ttk.Label(           
  frame,
  textvariable = following_var                           
  ).grid(
  column=1,                          
  row=6,                            
  sticky=(W, E))

#row 7
followers_label = ttk.Label(           
  frame,                           
  text='Followers:'
  ).grid(
  column=0,                          
  row=7,                            
  sticky=(W, E))                      

followers_var = StringVar()
followers_var.set(default_value)

followers = ttk.Label(           
  frame,
  textvariable = followers_var                           
  ).grid(
  column=1,                          
  row=7,                            
  sticky=(W, E))

#row 8
active_label = ttk.Label(           
  frame,                           
  text='Active:'
  ).grid(
  column=0,                          
  row=8,                            
  sticky=(W, E))                      

active_var = StringVar()
active_var.set(default_value)

active = ttk.Label(           
  frame,
  textvariable = active_var                           
  ).grid(
  column=1,                          
  row=8,                            
  sticky=(W, E))

#row 9
retrieve_at_label = ttk.Label(           
  frame,                           
  text='Retrieve at:'
  ).grid(
  column=0,                          
  row=9,                            
  sticky=(W, E))                      

retrieve_at_var = StringVar()
retrieve_at_var.set(default_value)

retrieve_at = ttk.Label(           
  frame,
  textvariable = retrieve_at_var                           
  ).grid(
  column=1,                          
  row=9,                            
  sticky=(W, E))

def read_form(*args):
    messagebox.showinfo(                            #from tkinter import messagebox
    title='Form Information', 
    message=f'Username: {username.get()}')
    reset_form()


def close():
    root.destroy()

def reset_form():
    pass
    #name.delete(0,END)
    #How can I unselected the radioButton

#row 5
# button = ttk.Button(
#     frame, 
#     text='Reset',
#     command=reset_form)          #buttons can also have images
# button.grid(
#     column=0, 
#     row=10, 
#     )#sticky=(W, E))

# ttk.Button(
#     frame, 
#     text='Ok',
#     width = 15,
#     command=read_form
#     ).grid(                        #the function that will be called
#     column=1, 
#     row=10, 
#     )#sticky=(W, E))

ttk.Button(
    frame, 
    text='Exit',
    command=close
    ).grid(                        #the delegate that will be called
    column=2, 
    row=10, 
    )#sticky=(W, E)) 

print("creating new instance")
client = mqtt.Client() #create new instance
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect('localhost', 1883) #connect to broker

print("Subscribing to topic","GROUP3")
client.subscribe('GROUP3')

 #Start the MQTT Mosquito process loop
client.loop_start() 

root.mainloop()

