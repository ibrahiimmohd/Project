#Lab8&9

from tkinter import Tk, Canvas, Frame, BOTH, W
import tkinter as tk

class Example(Frame):
    entryValue = "0"
    recHeight = 200

    def __init__(self):
        super().__init__()
        self.initUI()
        self.update()
    


    def initUI(self):
        self.master.title('Lab 9/10 Temperature')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(150, 200, 300, 200)    

        canvas.create_text(25, 220, anchor=W, font='Purisa', 
        text='Enter Value: ')
        
        entry1 = tk.Entry()
        canvas.create_window(220, 220, window=entry1)  
        self.entryValue = entry1.get()

        x = lambda a : a * 100

        def changeValue(text): 

            if(text == ''): 
                text = '1.5'
            else:
                text = text
            
            # temp = float(text)
            val = float(text) * 100
            self.recHeight = 200 - val
            canvas.coords(var, 200, 200, 250, self.recHeight)

            
           

        button1 = tk.Button(text='Change Value',
        command= lambda : changeValue(entry1.get())) #TODO: Add this to make functionality work - , command=changeValue
        canvas.create_window(340, 220, window=button1)

        var = canvas.create_rectangle(200, 200, 250, self.recHeight,
        outline='#222', fill='#f76')

        canvas.create_line(150, 30, 150, 200)
        canvas.create_text(30, 190, anchor=W, font='Purisa', text='Low     0°C')
        canvas.create_text(30, 150, anchor=W, font='Purisa', text='Normal 0.5°C')
        canvas.create_text(30, 100, anchor=W, font='Purisa', text='Normal 1°C')
        canvas.create_text(30, 50, anchor=W, font='Purisa', text='High     1.5°C')


        canvas.pack(fill=BOTH, expand=1) 

        

root = tk.Tk()
ex = Example()
root.geometry('400x250+300+300')
root.mainloop()

