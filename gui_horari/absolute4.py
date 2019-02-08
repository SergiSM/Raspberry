#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageTk
from tkinter import Tk, BOTH, Canvas
from tkinter.ttk import Frame, Label, Style
import datetime as dt

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()            

    def initUI(self):        

        #valors obtinguts del horaris en html
        self.colors = [['silver', 'blue', 'green'], ['red','orange','yellow', 'green']]
        self.text = [['Assig1 as fdsf af', 'Comunicacions Industrials', 'Assig3'], ['Assig10', 'Assig22', 'Assig33', 'Asig44']]
        self.hores = [[1,2,3], [2,1,2,3]]

        self.controls = []

        #def clicked(*args):
        def clicked(event):
            #borro controls anteriors
            for c in self.controls:
                self.w.delete(c)    #delete(ALL)            

            cota = 480 / 5  # 480 ample, 5 dies
            print(str(cota))
            if event.y >= 0 and event.y <= cota:
                txt = "Divendres"            
                carregar_dia(0)
            if event.y >= cota and event.y <= cota*2:
                txt = "Dijous"
                carregar_dia(1)

            self.w.itemconfig(self.titol, text=txt)            
            print('Got object click', event.x, event.y)
            print(event.widget.find_closest(event.x, event.y))                        
            

        def carregar_dia(dia):           
            #colors = ['silver', 'blue', 'green']
            #text = ['Assig1', 'Assig2', 'Assig3']
            #hores = [1, 2, 3]
            #colors = self.colors[dia]
            #text = self.text[dia]
            #hores = self.hores[dia]
            text = ['Assig1', 'Assig2', 'Des', 'Assig3', "Assig4"]
            colors = ['silver', 'blue', 'green', 'yellow', 'red']
            hores_ini = ["08:00", "09:00", "10:00", "10:20", "15:30"]
            hores_fi = ["09:00", "10:00", "10:20", "12:20", "16:30"]            
            pixels_minut = 50/60 #1 hora = 60 min = 50 píxels, 1 min = 50/60 = 0.83 (millor que sigui exacte)
            
            left = 50 #començant a les 8 del matí
               
            for i in range(len(hores_ini)):
                start_dt = dt.datetime.strptime("08:00", '%H:%M')
                end_dt = dt.datetime.strptime(hores_ini[i], '%H:%M')
                diff_inici = (end_dt - start_dt).seconds/60   
                print(diff_inici)

                inici_assig = diff_inici*pixels_minut
                print(inici_assig)

                start_dt = dt.datetime.strptime(hores_ini[i], '%H:%M')
                end_dt = dt.datetime.strptime(hores_fi[i], '%H:%M')
                diff_ample = (end_dt - start_dt).seconds/60   
                print(diff_ample)

                ample_assig = diff_ample*pixels_minut
                print(ample_assig)
                
                r = self.w.create_rectangle(left + inici_assig, 0, (left + inici_assig) + ample_assig, 380, fill=colors[i], outline = 'black')
                self.controls.append(r)                
                t = self.w.create_text(left + inici_assig + 20, 200 + 2.5*len(text[i]), anchor = 'nw', text=text[i], fill='black', font=('Arial', '10','bold'), angle=90)
                self.controls.append(t)                

            '''for h in hores:
                r = self.w.create_rectangle(left, 0, left+ h*ample, 380, fill=colors[i], outline = 'black')
                self.controls.append(r)                
                t = self.w.create_text(left + 20, 200 + 2.5*len(text[i]), anchor = 'nw', text=text[i], fill='black', font=('Arial', '10','bold'), angle=90)
                self.controls.append(t)
                left = left + h*ample
                i = i + 1 '''               

        #self.master.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        
        #Style().configure("TFrame", background="#333")
        
        '''
        rot = Image.open("verd.png")
        rot_ = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rot_)
        label2.image = rot_
        label2.place(x=40, y=160) '''                     

        self.w = Canvas(self, width=800, height=480, bg="black")
        #w.pack()

        self.w.create_rectangle(0, 0, 50, 480, fill='blue', outline = 'black')
        self.titol = self.w.create_text(20, 200, text="Divendres", fill='white', font=('Arial', '12','bold'), angle=90)
        
        top = 0   
        ample = 50
        llarg = 100
        left = 50   
        hh = ["08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "17:00 - 18:00", "18:00 - 19:00", "19:00 - 20:00"]        
        for i in range(12): 
            self.w.create_rectangle(left, 380, left + ample, 480, fill='silver', outline = 'black')  #outline=border            
            self.w.create_text(left+20, 430, anchor = 'center', text=hh[i], fill='black', font=('Arial', '10','bold'), angle=90)                        
            left = left + ample

        #carregar_dia(0)
        #self.controls = []
        '''mida_dia = 100
        colors = ['silver', 'blue', 'green']
        text = ['Assig1', 'Assig2', 'Assig3']
        hores = [1, 2, 3]
        i = 0
        top = 0
        left = 50
        for h in hores:
            r = self.w.create_rectangle(left, 0, left+ h*ample, 380, fill=colors[i], outline = 'black')
            self.controls.append(r)
            t = self.w.create_text(left + 20, 200, anchor = 'nw', text=text[i], fill='black', font=('Arial', '10','bold'), angle=90)
            self.controls.append(t)
            left = left + h*ample
            i = i + 1'''

        #posar imatges per centrar els labels
        '''top = 0
        ample = 480/5
        dies = ['Divendres', 'Dijous', 'Dimecres', 'Dimarts', 'Dilluns']
        for i in range(5):
            playbutton = w.create_rectangle(700, top, 800, top + (i+1)*ample, fill='blue', outline = 'black', tags="playbutton")
            w.create_text(750, top + 60, text=dies[i], fill='black', font=('Arial', '10','bold'), angle=90)
            top = (i+1)*ample

        w.tag_bind("playbutton","<Button-1>", clicked)'''

        top = 0
        ample = 480/5

        self.w.create_rectangle(720, top, 800, top + int(ample), fill='blue', outline = 'white', tags="playbutton")
        self.w.tag_bind("playbutton","<Button-1>", clicked)
        self.w.create_text(760, top + 45, text="Divendres", fill='white', font=('Arial', '12','bold'), angle=90, tags="playbutton")
        top = top + ample

        self.w.create_rectangle(720, top, 800, top + int(ample), fill='blue', outline = 'black', tags="playbutton")
        self.w.tag_bind("playbutton","<Button-1>", clicked)
        self.w.create_text(760, top + 50, text="Dijous", fill='white', font=('Arial', '12','bold'), angle=90, tags="playbutton")
        top = top + ample

        self.w.create_rectangle(720, top, 800, top + int(ample), fill='blue', outline = 'black', tags="playbutton")
        self.w.tag_bind("playbutton","<Button-1>", clicked)
        self.w.create_text(760, top + 50, text="Dimecres", fill='white', font=('Arial', '12','bold'), angle=90, tags="playbutton")
        top = top + ample

        self.w.pack()

def main():
  
    root = Tk()
    root.geometry("800x480+0+0")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
