#group_3_subscriber_proj2.py
from tkinter import Tk, Canvas, Frame, BOTH, W, TOP, BOTTOM
import tkinter as tk
import random
import time
import threading
import paho.mqtt.client as mqtt
import group_3_util_proj as util
import json

SUBSCRIBE_TOPIC = 'GROUP3'
HOST = 'localhost'
PORT = 1883

class Example(Frame):
    RECT_WIDTH = 50
    canvas = None
    Y_AXIS = 400 
    X_AXIS = 150
    RECT_COLOR = '#28A745'
    RECT_OUTLINE_COLOR = '#222'
    rect_list = list()
    time_stamp = None
    rect_height = [
        Y_AXIS,
        Y_AXIS,
        Y_AXIS,
        Y_AXIS,
        Y_AXIS,
        Y_AXIS,
        Y_AXIS,
    ]

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Human Body Temperature')
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self) 

        # create coordinate y-axis
        self.canvas.create_line(self.X_AXIS, 80, self.X_AXIS, self.Y_AXIS)
        # create coordinate x-axis
        self.canvas.create_line(self.X_AXIS, self.Y_AXIS, 500, self.Y_AXIS)

        self.time_stamp = self.canvas.create_text(self.X_AXIS+150,self.Y_AXIS+20,fill="#FFB6C1",font="Times 12 italic bold")

        #initialize 7 rectangle with empty height
        for x in range(7):
            rec = self.canvas.create_rectangle(
                self.X_AXIS + x*self.RECT_WIDTH, 
                self.Y_AXIS, 
                self.X_AXIS + (x+1)*self.RECT_WIDTH, 
                self.Y_AXIS, 
                outline=self.RECT_OUTLINE_COLOR,fill=self.RECT_COLOR)
            self.rect_list.append(rec)

        self.canvas.pack(fill=BOTH, expand=1)

    def drawRectangle(self,canvas,height):
        for x in range(6):
            self.rect_height[x] = self.rect_height[x+1]
        self.rect_height[6] = height

        for x in range(7):
            canvas.coords(self.rect_list[x], self.X_AXIS + x*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + (x+1)*self.RECT_WIDTH,self.rect_height[x])

             
root = tk.Tk()
ex = Example()
root.geometry('600x450+300+300')


def on_message(client, userdata, message):
    data = message.payload.decode('utf-8')
    try:
        obj = json.loads(data)
        util.print_data(obj)
        # Because Human temp is always greater than 30*C
        # So will only take the units column
        # But the units column is small ~ 7
        # So multiply by 40 to indicate better the different
        ex.drawRectangle(ex.canvas,ex.Y_AXIS - (obj['body_temp'] - 30) * 40)
        # Update time stamp label
        ex.canvas.itemconfigure(ex.time_stamp, text="Last update: "+obj['retrieve_at'])
    except:
        ex.drawRectangle(ex.canvas,ex.Y_AXIS)
    

print("creating new instance")
client = mqtt.Client() #create new instance
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(HOST,PORT) #connect to broker

print("Subscribing to topic ",SUBSCRIBE_TOPIC)
client.subscribe(SUBSCRIBE_TOPIC)

#Start the MQTT Mosquito process loop
client.loop_start()
root.mainloop()


