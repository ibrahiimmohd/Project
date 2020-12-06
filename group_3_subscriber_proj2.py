#group_3_subscriber_proj2.py
from tkinter import Tk, Canvas, Frame, BOTH, W
import tkinter as tk
import random
from tkinter.ttk import Button
from tkinter import Tk, Canvas, Frame, BOTH, W, TOP, BOTTOM
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
    rec1 = None
    rec2 = None
    rec3 = None
    rec4 = None
    rec5 = None
    rec6 = None
    rec7 = None
    time_stamp = None
    rect_height = {
        "rect1": Y_AXIS,
        "rect2": Y_AXIS,
        "rect3": Y_AXIS,
        "rect4": Y_AXIS,
        "rect5": Y_AXIS,
        "rect6": Y_AXIS,
        "rect7": Y_AXIS,
    }

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

        self.time_stamp = self.canvas.create_text(self.X_AXIS+150,self.Y_AXIS+20,fill="darkblue",font="Times 12 italic bold",
                        text="")

        #initialize 7 rectangle with empty height
        self.rec1 = self.canvas.create_rectangle(self.X_AXIS + 0*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 1*self.RECT_WIDTH, self.Y_AXIS, outline=self.RECT_OUTLINE_COLOR, fill=self.RECT_COLOR)
        self.rec2 = self.canvas.create_rectangle(self.X_AXIS + 1*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 2*self.RECT_WIDTH, self.Y_AXIS, outline=self.RECT_OUTLINE_COLOR, fill=self.RECT_COLOR)
        self.rec3 = self.canvas.create_rectangle(self.X_AXIS + 2*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 3*self.RECT_WIDTH, self.Y_AXIS, outline=self.RECT_OUTLINE_COLOR, fill=self.RECT_COLOR)
        self.rec4 = self.canvas.create_rectangle(self.X_AXIS + 3*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 4*self.RECT_WIDTH, self.Y_AXIS, outline=self.RECT_OUTLINE_COLOR, fill=self.RECT_COLOR)
        self.rec5 = self.canvas.create_rectangle(self.X_AXIS + 4*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 5*self.RECT_WIDTH, self.Y_AXIS, outline=self.RECT_OUTLINE_COLOR, fill=self.RECT_COLOR)
        self.rec6 = self.canvas.create_rectangle(self.X_AXIS + 5*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 6*self.RECT_WIDTH, self.Y_AXIS, outline=self.RECT_OUTLINE_COLOR, fill=self.RECT_COLOR)
        self.rec7 = self.canvas.create_rectangle(self.X_AXIS + 6*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 7*self.RECT_WIDTH, self.Y_AXIS, outline=self.RECT_OUTLINE_COLOR, fill=self.RECT_COLOR)

        self.canvas.pack(fill=BOTH, expand=1)

    def drawRectangle(self,canvas,height):

        self.rect_height["rect1"] = self.rect_height["rect2"]
        self.rect_height["rect2"] = self.rect_height["rect3"]
        self.rect_height["rect3"] = self.rect_height["rect4"]
        self.rect_height["rect4"] = self.rect_height["rect5"]
        self.rect_height["rect5"] = self.rect_height["rect6"]
        self.rect_height["rect6"] = self.rect_height["rect7"]
        self.rect_height["rect7"] = height

        canvas.coords(self.rec1, self.X_AXIS + 0*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 1*self.RECT_WIDTH,self.rect_height["rect1"])
        canvas.coords(self.rec2, self.X_AXIS + 1*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 2*self.RECT_WIDTH,self.rect_height["rect2"])
        canvas.coords(self.rec3, self.X_AXIS + 2*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 3*self.RECT_WIDTH,self.rect_height["rect3"])
        canvas.coords(self.rec4, self.X_AXIS + 3*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 4*self.RECT_WIDTH,self.rect_height["rect4"])
        canvas.coords(self.rec5, self.X_AXIS + 4*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 5*self.RECT_WIDTH,self.rect_height["rect5"])
        canvas.coords(self.rec6, self.X_AXIS + 5*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 6*self.RECT_WIDTH,self.rect_height["rect6"])
        canvas.coords(self.rec7, self.X_AXIS + 6*self.RECT_WIDTH, self.Y_AXIS, self.X_AXIS + 7*self.RECT_WIDTH,self.rect_height["rect7"])

             
root = tk.Tk()
ex = Example()
root.geometry('600x450+300+300')


def on_message(client, userdata, message):
    data = message.payload.decode('utf-8')
    try:
        obj = json.loads(data)
        util.print_data(obj)
        ex.drawRectangle(ex.canvas,ex.Y_AXIS - (obj['body_temp'] - 30) * 40)
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
# while True:
#  client.loop_forever()


