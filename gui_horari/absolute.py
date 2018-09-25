#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageTk
from tkinter import Tk, BOTH, Canvas
from tkinter.ttk import Frame, Label, Style

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()

        
    def initUI(self):
      
        #self.master.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        
        #Style().configure("TFrame", background="#333")
        
        '''
        rot = Image.open("verd.png")
        rot_ = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rot_)
        label2.image = rot_
        label2.place(x=40, y=160) '''     
        
        w = Canvas(self, width=800, height=480, bg="black")
        w.pack()

        top = 0   
        ample = 40
        llarg = 100
        cota1 = llarg     
        hh = ["08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "17:00 - 18:00", "18:00 - 19:00", "19:00 - 20:00"]        
        for i in range(12): 
            w.create_rectangle(0, top, cota1, top+ample, fill='silver', outline = 'black')  #outline=border
            w.create_text(50, top + 20, anchor = 'center', text=hh[i], fill='black', font=('Arial', '10','bold'))
            #label1 = Label(w, text=hh[i], font=('MS', 8, 'bold'))
            #label1.place(x=15, y=top+15)
            top = top + ample

        mida_dia = 100
        colors = ['silver', 'blue', 'green']
        text = ['Assig1', 'Assig2', 'Assig3']
        hores = [1, 2, 3]
        i = 0
        top = 0
        cota2 = cota1 + mida_dia
        for h in hores:
            w.create_rectangle(cota1, top, cota2, top + h*ample, fill=colors[i], outline = 'black')
            w.create_text(cota1 + 50, top + 20, anchor = 'center', text=text[i], fill='black', font=('Arial', '10','bold'))        
            top = top + h*ample
            i = i + 1

        colors = ['silver', 'blue', 'green']
        text = ['Assig1', 'Assig2', 'Assig3']
        hores = [3, 4, 1]
        i = 0
        top = 0
        cota3= cota2 + mida_dia
        for h in hores:
            w.create_rectangle(cota2, top, cota3, top + h*ample, fill=colors[i], outline = 'black')
            w.create_text(cota2 + 50, top + 20, anchor = 'center', text=text[i], fill='black', font=('Arial', '10','bold'))        
            top = top + h*ample
            i = i + 1

def main():
  
    root = Tk()
    root.geometry("800x480+300+300")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
