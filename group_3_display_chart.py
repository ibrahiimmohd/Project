#Lab11

from tkinter import Tk, Canvas, Frame, BOTH, W
import tkinter as tk
import random

class Example(Frame):
    entryValue = "0"
    recHeight = 300
    rangeTag = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""

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
        
        randomList = []
        for x in range(20):
            randomList.append(int(random.randint(80,200)))
        for j in range(len(randomList)):
            if(randomList[j] in range(0,100)):
                self.d1+=1
            elif(randomList[j] in range(101,120)):
                self.d2+=1
            elif(randomList[j] in range(121,140)):
                self.d3+=1
            elif(randomList[j] in range(141,160)):
                self.d4+=1
            elif(randomList[j] in range(161,180)):
                self.d5+=1
            elif(randomList[j] in range(181,200)):
                self.d6+=1

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
            
            high = int(text)
            low = high - 5
            rangeTxt = str('0' if low < 0 else low)+'-'+str(high)

            cal1 = (self.recHeight)-(int(self.d1) * 50)
            cal2 = (self.recHeight)-(int(self.d2) * 50)
            cal3 = (self.recHeight)-(int(self.d3) * 50)
            cal4 = (self.recHeight)-(int(self.d4) * 50)
            cal5 = (self.recHeight)-(int(self.d5) * 50)
            cal6 = (self.recHeight)-(int(self.d6) * 50)

            check1 = cal1 if self.d1 in range(low,high) else self.recHeight
            check2 = cal2 if self.d2 in range(low,high) else self.recHeight
            check3 = cal3 if self.d3 in range(low,high) else self.recHeight
            check4 = cal4 if self.d4 in range(low,high) else self.recHeight
            check5 = cal5 if self.d5 in range(low,high) else self.recHeight
            check6 = cal6 if self.d6 in range(low,high) else self.recHeight

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

