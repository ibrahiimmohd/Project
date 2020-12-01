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
        self.master.title('Lab 9 and 10 A & B')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(150, 200, 300, 200)    

        canvas.create_text(25, 200, anchor=W, font='Purisa', 
        text='Enter Value: ')
        
        entry1 = tk.Entry()
        canvas.create_window(75, 220, window=entry1)  
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
        canvas.create_window(200, 220, window=button1)

        var = canvas.create_rectangle(200, 200, 250, self.recHeight,
        outline='#222', fill='#f76')

        canvas.create_line(150, 30, 150, 200)
        canvas.create_text(140, 200, anchor=W, font='Purisa', text='0')
        canvas.create_text(127, 150, anchor=W, font='Purisa', text='0.5')
        canvas.create_text(140, 100, anchor=W, font='Purisa', text='1')
        canvas.create_text(127, 50, anchor=W, font='Purisa', text='1.5')


        canvas.pack(fill=BOTH, expand=1) 

        

root = tk.Tk()
ex = Example()
root.geometry('400x250+300+300')
root.mainloop()

