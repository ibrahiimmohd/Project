from tkinter import Tk, Canvas, Frame, BOTH, W
import tkinter as tk

class Example(Frame):
    entryValue = "0"
    recHeight = 230

    def __init__(self):
        super().__init__()
        self.initUI()
    
    

    def initUI(self):
        self.master.title('Lab 9/10 Temperature')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)   

        canvas.create_text(25, 200, anchor=W, font='Purisa', 
        text='Enter Value: ')

        canvas.create_text(55, 50, anchor=W, font='Purisa', 
        text='Unit in °C')
        
        entry1 = tk.Entry()
        canvas.create_window(75, 220, window=entry1)  
        self.entryValue = entry1.get()
        

        def changeValue(text):  
            if(text == ''): 
                text = '0'
            else:
                text = text
            
            # temp = float(text)
            val = float(text) * 45
            self.recHeight = 230 + val
            canvas.coords(var, self.recHeight, 90, 275, 130)


        button1 = tk.Button(text='Change Value',command= lambda : changeValue(entry1.get())) #TODO: Add this to make functionality work - , command=changeValue
        canvas.create_window(200, 220, window=button1)

        canvas.create_oval(210, 50,   #top left
        350, 190,                      #bottom right
        outline='#000', fill='', width=2)

        canvas.create_text(230, 90, anchor=W, font='Purisa', text='0')
        canvas.create_text(320, 90, anchor=W, font='Purisa', text='2')
        canvas.create_text(275, 70, anchor=W, font='Purisa', text='1')
        canvas.create_text(252.5, 80, anchor=W, font='Purisa', text='.5')
        canvas.create_text(292.5, 80, anchor=W, font='Purisa', text='1.5')

        var = canvas.create_line(self.recHeight, 90, 275, 130)

        canvas.pack(fill=BOTH, expand=1) 

        

root = tk.Tk()
ex = Example()
root.geometry('400x250+300+300')
root.mainloop()