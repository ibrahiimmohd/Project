#Lab8&9

from tkinter import Tk, Canvas, Frame, BOTH, W
import tkinter as tk

class Example(Frame):
    entryValue = "0"
    recHeight = 50

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def changeValue(self):  
        # x1 = self.entryValue
        self.recHeight = int(self.entryValue)

    def initUI(self):
        self.master.title('Lab 9 and 10 A & B')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(150, 200, 300, 200)    

        canvas.create_text(25, 200, anchor=W, font='Purisa', 
        text='Enter Value: ')
                 
             
        entry1 = tk.Entry(root)
        canvas.create_window(75, 220, window=entry1)  
        self.entryValue = entry1.get()

        button1 = tk.Button(text='Change Value',command=self.changeValue) #TODO: Add this to make functionality work - , command=changeValue
        canvas.create_window(200, 220, window=button1)

        canvas.create_rectangle(200, 200, 250, self.recHeight,
        outline='#222', fill='#f76')

        canvas.create_line(150, 30, 150, 200)
        canvas.pack(fill=BOTH, expand=1) 


root = tk.Tk()
ex = Example()
root.geometry('400x250+300+300')
root.mainloop()


'''
from tkinter import Tk, Canvas, Frame, BOTH, W

class Example(Frame):
    def __init__(self):        
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Lab 9 A & B')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)        
        canvas.create_line(15, 25,     #start x,y
        200, 25)                       #end x,y
        
        canvas.create_line(300, 35, 300, 200,         dash=(4, 2))                   #line style        
        canvas.create_line(55, 85,     #first point
        155, 85,                       #second point
        105, 180,                      #third point
        55, 85)                        #back to first point        
        
        canvas.create_arc(200, 100,    #top left
        260, 160,                      #bottom right        
        start=45, extent=135,          #start angle how far to go        
        outline='#77f', fill='#f11', width=2)        
        
        canvas.create_oval(200, 150, 280, 230, 
        outline='#f11', 
        fill='#1f1', 
        width=2)        
        
        canvas.create_rectangle(320, 140,                  #top left
        370, 190,                  #bottom right        
        outline='#222', 
        fill='#f76')        
        
        canvas.create_text(20, 220, 
        anchor=W, 
        font='Purisa',         
        text='Narendra is the greatest!')        
        
        canvas.pack(fill=BOTH, expand=1)

root = Tk()
ex = Example()
root.geometry('400x250+300+300')
root.mainloop()
'''