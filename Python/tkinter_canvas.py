#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
import sys
import time

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

class Fullscreen_Window:        

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes("-fullscreen", True)  
        #if platform.system() == "Windows":   
        #    self.tk.wm_state("zoomed") #maximitzat
        #self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        #self.tk.configure(background='#353F4B', cursor='none')

        self.photo = PhotoImage(file="fons0.png")

        self.canvas = Canvas(self.tk, width=800, height=480, background="blue", bd=0, highlightthickness=0)
        imatge = self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.grid(row=0, column=0, sticky="ew")

        self.l_hora = self.canvas.create_text(400, 125, text='MODUL WIFI NO DETECTAT', font=("Helvetica", 28), fill='#000000')        

        self.img_new = PhotoImage(file="new.png")
        self.canvas.create_image(10, 200, anchor=NW, image=self.img_new)

        self.canvas.create_line(15, 25, 200, 25)
        self.canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        self.canvas.create_rectangle(30, 100, 120, 180, outline="#fb0", fill="#fb0")
        self.canvas.create_rectangle(150, 100, 240, 180, outline="#f50", fill="#f50")
        self.canvas.create_rectangle(270, 100, 370, 180, outline="#05f", fill="#05f")
        self.canvas.create_oval(10, 10, 80, 80, outline="#f11", fill="#1f1", width=2)
        self.canvas.create_oval(110, 10, 210, 80, outline="#f11", fill="#1f1", width=2)
        self.canvas.create_rectangle(230, 10, 290, 60, outline="#f11", fill="#1f1", width=2)
        self.canvas.create_arc(30, 200, 90, 100, start=0, extent=210, outline="#f11", fill="#1f1", width=2)
            
        points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
        self.canvas.create_polygon(points, outline='#f11', fill='#1f1', width=2)  

        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

        def printcoords(event):            
            print (event.x,event.y)
            if (((event.x >=15) and (event.x <=65)) and ((event.y >=208) and (event.y <=254))):
                self.canvas.itemconfig(imatge, image=self.photo)                
                self.canvas.itemconfig(self.l_hora, text="********************************************")

            if (((event.x >=70) and (event.x <=135)) and ((event.y >=374) and (event.y <=444))):                
                self.apagar_raspberry()
                    
                
        self.canvas.bind("<Button 1>",printcoords)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)			
        return "break"

    def update_clock(self):
        now = time.strftime("%H:%M:%S")           
        #self.l_hora["text"] = str(now)
        #self.l_hora.configure(text=now)
        self.canvas.itemconfig(self.l_hora, text=now)
        self.tk.after(1000, self.update_clock)

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.toggle_fullscreen()
    w.update_clock()  
    w.tk.mainloop()
