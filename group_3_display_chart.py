#Lab11

from tkinter import Tk, Canvas, Frame, BOTH, W
import tkinter as tk
import random
from tkinter.ttk import Button
from tkinter import Tk, Canvas, Frame, BOTH, W, TOP, BOTTOM
import time
import threading

class Example(Frame):
    entryValue = "0"
    recHeight = 300
    randomList = []
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0

    def __init__(self):
        super().__init__()
        self.initUI()
        self.update()
                

    def initUI(self):
        self.master.title('Lab 12')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        button = Button(root, text= 'Go')
        button.pack(side= TOP, pady = 5)  
        for x in range(20):
            self.randomList.append(int(random.randint(80,200)))

        def goButton():
            t = threading.Thread(target=changeValue())
            t.setDaemon(True)

        def changeValue(): 

            for x in range(0, 20):
                self.randomList.pop(0)
                self.randomList.append(int(random.randint(80,200)))
                
                cal1 = self.recHeight - self.randomList[0]
                cal2 = self.recHeight - self.randomList[1]
                cal3 = self.recHeight - self.randomList[2]
                cal4 = self.recHeight - self.randomList[3]
                cal5 = self.recHeight - self.randomList[4]
                cal6 = self.recHeight - self.randomList[5]

                print(cal1, cal2, cal3, cal4, cal5, cal6)

                canvas.coords(line1, 225, cal2 , 175, cal1)
                canvas.coords(line2, 275, cal3, 225, cal2)
                canvas.coords(line3, 325, cal4 , 275, cal3)
                canvas.coords(line4, 375, cal5 , 325, cal4)
                canvas.coords(line5, 425, cal6 , 375, cal5)
                time.sleep(0.5)
                print('Loop number: {}'.format(x))

                canvas.coords(var1, 150, 300, 200, cal1 )
                canvas.coords(var2, 200, 300, 250, cal2 )
                canvas.coords(var3, 250, 300, 300, cal3 )
                canvas.coords(var4, 300, 300, 350, cal4 )
                canvas.coords(var5, 350, 300, 400, cal5 )
                canvas.coords(var6, 400, 300, 450, cal6 )   
                root.update()            
        

        button1 = tk.Button(text='Go', width=10,command= lambda : goButton())
        canvas.create_window(340, 20, window=button1)

        var1 = canvas.create_rectangle(150, 300, 200, self.recHeight,
        outline='#222', fill='#f76')

        var2 = canvas.create_rectangle(200, 300, 250, self.recHeight,
        outline='#222', fill='#f76')

        var3 = canvas.create_rectangle(250, 300, 300, self.recHeight,
        outline='#222', fill='#f76')

        var4 = canvas.create_rectangle(300, 300, 350, self.recHeight,
        outline='#222', fill='#f76')

        var5 = canvas.create_rectangle(350, 300, 400, self.recHeight,
        outline='#222', fill='#f76')

        var6 = canvas.create_rectangle(400, 300, 450, self.recHeight,
        outline='#222', fill='#f76')

        line1 = canvas.create_line(225, 0 , 175, 0)
        line2 = canvas.create_line(275, 0, 225, 0)
        line3 = canvas.create_line(325, 0 , 275, 0)
        line4 = canvas.create_line(375, 0 , 325, 0)
        line5 = canvas.create_line(425, 0 , 375, 0)

        canvas.create_line(150, 80, 150, 300)
        

        canvas.pack(fill=BOTH, expand=1) 
        
        
   
        
root = tk.Tk()
ex = Example()
root.geometry('600x450+300+300')
root.mainloop()

