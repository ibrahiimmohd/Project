#Lab11

from tkinter import Tk, Canvas, Frame, BOTH, W
import tkinter as tk
import random

class Example(Frame):
    entryValue = "0"
    recHeight = 300
    randomList = []
    rangeTag = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""

    def __init__(self):
        super().__init__()
        self.initUI()
        self.update()
        
        for x in range(20):
            self.randomList.append(int(random.randint(0,20)))

    def initUI(self):
        self.master.title('Lab 11 Temperature')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        canvas.create_text(25, 20, anchor=W, font='Purisa', 
        text='Data range: ')

        canvas.create_text(45, 60, anchor=W, font='Purisa', 
        text='Data range: ')
        
        entry1 = tk.Entry()
        canvas.create_window(220, 20, window=entry1)  
        self.entryValue = entry1.get()

        def changeValue(text): 
            
            if(int(text) <= 19):
                high = int(text)
                low = high - 5
                rangeTxt = str('0' if low < 0 else low)+'-'+str(high)

                check1 = (self.recHeight)-(self.randomList[low] * 10) 
                check2 = (self.recHeight)-(self.randomList[low+1] * 10)
                check3 = (self.recHeight)-(self.randomList[low+2] * 10)
                check4 = (self.recHeight)-(self.randomList[low+3] * 10)
                check5 = (self.recHeight)-(self.randomList[low+4] * 10)
                check6 = (self.recHeight)-(self.randomList[low+5] * 10)

                if(self.rangeTag == ''):
                    self.rangeTag = canvas.create_text(155, 60, anchor=W, font='Purisa', text = rangeTxt, tag="rangeTag")
                    self.line1 = canvas.create_line(225, check2, 175, check1)
                    self.line2 = canvas.create_line(275, check3, 225, check2)
                    self.line3 = canvas.create_line(325, check4, 275, check3)
                    self.line4 = canvas.create_line(375, check5, 325, check4)
                    self.line5 = canvas.create_line(425, check6, 375, check5)
                else:
                    canvas.delete(self.rangeTag)
                    canvas.delete(self.line1)
                    canvas.delete(self.line2)
                    canvas.delete(self.line3)
                    canvas.delete(self.line4)
                    canvas.delete(self.line5)

                    self.rangeTag = canvas.create_text(155, 60, anchor=W, font='Purisa', text = rangeTxt, tag="rangeTag")
                    self.line1 = canvas.create_line(225, check2, 175, check1)
                    self.line2 = canvas.create_line(275, check3, 225, check2)
                    self.line3 = canvas.create_line(325, check4, 275, check3)
                    self.line4 = canvas.create_line(375, check5, 325, check4)
                    self.line5 = canvas.create_line(425, check6, 375, check5)

                canvas.coords(var1, 150, 300, 200, check1)
                canvas.coords(var2, 200, 300, 250, check2)
                canvas.coords(var3, 250, 300, 300, check3)
                canvas.coords(var4, 300, 300, 350, check4)
                canvas.coords(var5, 350, 300, 400, check5)
                canvas.coords(var6, 400, 300, 450, check6)
            else:
                canvas.delete(self.rangeTag)
                rangeTxt = 'Please select appropriate range'
                self.rangeTag = canvas.create_text(155, 60, anchor=W, font='Purisa', text = rangeTxt, tag="rangeTag")

            
 
        button1 = tk.Button(text='Go', width=10,
        command= lambda : changeValue(entry1.get()))
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

        canvas.create_line(150, 80, 150, 300)

        canvas.pack(fill=BOTH, expand=1) 

        
root = tk.Tk()
ex = Example()
root.geometry('600x450+300+300')
root.mainloop()

