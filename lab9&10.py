#this is new change
#this is second change


from tkinter import Tk, Canvas, Frame, BOTH, W
import tkinter as tk

class Example(Frame):
    entryValue = "0"
    recHeight = 50

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def changeValue(self):  
        x1 = self.entryValue
        self.recHeight = int(x1)

    def initUI(self):
        self.master.title('Lab 9 and 10 A & B')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(150, 200, 300, 200)    

        canvas.create_text(25, 200, anchor=W, font='Purisa', 
        text='Enter Value: ')
                 
             
        entry1 = tk.Entry (root)
        canvas.create_window(75, 220, window=entry1)  
        self.entryValue = entry1.get

        button1 = tk.Button(text='Change Value') #TODO: Add this to make functionality work - , command=changeValue
        canvas.create_window(200, 220, window=button1)

        canvas.create_rectangle(200, 200, 250, self.recHeight,
        outline='#222', fill='#f76')

        canvas.create_line(150, 30, 150, 200)
        canvas.pack(fill=BOTH, expand=1) 


    
        
        
    
root = tk.Tk()
ex = Example()
root.geometry('400x250+300+300')
root.mainloop()

