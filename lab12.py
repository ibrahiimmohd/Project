from tkinter import Tk, Canvas, Frame, BOTH, W, TOP, BOTTOM
import tkinter as tk
from tkinter.ttk import Button
import matplotlib.pyplot as plt
import random
import time
import threading

#Data from lab 8:
class Simulator:

    def __init__(self, base = 10, delta = 0.15):
        self.base = base
        self.delta = delta

    def generator_4(self, increment = True) -> float:
        if increment:
            self.base += random.gauss(0, 0.1) #self.delta
        else:
            self.base -= random.gauss(0, 0.1) #self.delta
        return self.base
        
number_of_values = 350 #random.randint(0,500)

test = Simulator(0) #Simulator(10, 0.15)    
#y = [test.generator_4((x % 50) > 24) for x in range(number_of_values)]
def generatorPlots():
    for x in range(number_of_values):
        time.sleep(3)
        y = test.generator_4((x % 50) > 24)
        x = random.randint(0,500)
        #print(x,y)

list_of_values = []
def generate_values():
    #x = 0
    s = ''
    while True:
        x = random.randint(0,100)
        #s += (str(x) + ' ')
        print(x)
        list_of_values.append(x)
        time.sleep(0.5)
    #return list_of_values
#x = 0 



#Create a thread?

class Example(Frame):

    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
    #def createLine(self):
    #    x1 = random.randint(20,200)
    #    y1 = random.randint(20,200)
    #    x2 = random.randint(20,200) 
    #    y2 = random.randint(20,200)
    #    Canvas.create_line(x1,y1,x2,y2, fill="blue")
    

    def initUI(self):
        self.master.title('Lab 12')
        self.pack(fill=BOTH, expand=1)

        #canvas = Canvas()
        canvas = tk.Canvas(width=800, height=400, bg="Pink1")
        
        #Threading to print the values on the console when the GUI is still running
        t = threading.Thread(target=generate_values)
        t.setDaemon(True)
        def createLine():
            x1 = random.randint(20,200)
            y1 = random.randint(20,200)
            x2 = random.randint(20,200) 
            y2 = random.randint(20,200)
            canvas.create_line(x1,y1,x2,y2, fill="blue")
        
        ##When button is click, new line is created
        button = Button(root, text= 'Go', command=createLine)
        button.pack(side= TOP, pady = 5)   
        t.start()

        

        
        #(left,top,right,bottom)
        ## right must be > left
        ##The connecting point: right line 1 == left line 1, bottom line 1 == top line 2
        #use while loop? or do while?
        # x1, y1 --- x2, y2 --- x3,y3
        # x1 < x2 < x3  @@Steps between y should not be too big so that the curves would look nicer
        #line 1 x3,y3 == line 2 x1,y1
        # initial x1 = 0 (so that the line start from the left axis)
        # initial y1 can be random
        #canvas.create_line(x1, y1,x2,y2, x3, y3, smooth=True, fill="blue")
        #createLine(x1,y1,x2,y2, x3, y3)
        #canvas.create_line(x3, y3, x4, y4, x5, y5, smooth=True, fill="blue")
        #canvas.create_line(x5, y5, x6, y6, x7, y7, smooth=True, fill="blue")
        canvas.pack() 


    
        
        
    
root = tk.Tk()

root.geometry('900x400')
ex = Example()
#button = Button(root, text= 'Go', command=ex.createLine)
#button.pack(side= TOP, pady = 5) 


root.mainloop()