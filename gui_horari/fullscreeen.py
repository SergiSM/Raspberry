#!/usr/bin/env python
# -*- coding: utf-8 -*-
   
import socket
import time
import sys
import array
import os
import threading
import subprocess
import tkMessageBox

from comunicacio import *   #importo funcions del fitxer comunicacio.py

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

TCP_IP = '192.168.1.3'
TCP_PORT = 5000
BUFFER_SIZE = 1024
AUTENTICACIO = ""
'''CABAL_60 = ""    
CABAL_120 = ''
BYPASS_ON =  ''
BYPASS_OFF = '' '''

class Fullscreen_Window:    
    

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.tk.configure(background='#353F4B', cursor='none')
        '''self.frame = Frame(self.tk)
        self.frame.configure(background='#353F4B')
        self.frame.pack()'''        

        self.estat_bypass = 0

        '''self.l_ssid = Label(self.tk, text = "MODUL WIFI NO DETECTAT", font=("Helvetica", 28), fg="#9A9FA5")
        self.l_ssid.configure(background="#353F4B")
        self.l_ssid.pack()'''

        self.photo = PhotoImage(file="fons0.png")   #com que crido script des de /etc/xdg/lxsession/LXDE/autostart indico ruta sencera
        self.photo2 = PhotoImage(file="fons1.png")
        self.photo3 = PhotoImage(file="fons2.png")
        self.photo4 = PhotoImage(file="fons3.png")

        self.canvas = Canvas(self.tk,width=800, height=480, background="#00FF00", bd=0, highlightthickness=0)
        imatge = self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.l_ssid = self.canvas.create_text(400, 25, text='MODUL WIFI NO DETECTAT', font=("Helvetica", 28), fill='#9A9FA5')
        self.canvas.pack()      
	    
        def printcoords(event):            
            print (event.x,event.y)
            if (((event.x >=215) and (event.x <=305)) and ((event.y >=155) and (event.y <=217))):
                self.canvas.itemconfig(imatge, image=self.photo)                
                #self.domeo("60")
                canvi_cabal(60)

            if (((event.x >=348) and (event.x <=438)) and ((event.y >=73) and (event.y <=155))):
                self.canvas.itemconfig(imatge, image=self.photo2)
                #self.domeo("120")
                canvi_cabal(120)

            if (((event.x >=485) and (event.x <=585)) and ((event.y >=155) and (event.y <=217))):
                if (self.estat_bypass == 0):
                    self.canvas.itemconfig(imatge, image=self.photo3)
                    activacio_bypass(True)
                    #self.domeo("bypass on")
                    self.estat_bypass = 1
                else:                    
                    self.canvas.itemconfig(imatge, image=self.photo4)
                    activacio_bypass(False)
                    #self.domeo("bypass off")
                    self.estat_bypass = 0

            if (((event.x >=70) and (event.x <=135)) and ((event.y >=374) and (event.y <=444))):                
                self.apagar_raspberry()
                    
                
        self.canvas.bind("<Button 1>",printcoords) 

        ''' ///
        back_img = PhotoImage(file="fons.gif")
        back_label= Label(self.frame, image=back_img)
        back_label.place(x=220, y=0, relwidth=1, relheight=1)
        back_label.pack()
                
        canvas = Canvas(self.tk,width=800, height=480)
        imatge = canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.pack() ///
        '''
        
        
        
        '''button = Button(self.frame, text="Cabal 60", command=lambda: self.domeo("60"))        
        button.pack(padx=20,pady=20)
        button2 = Button(self.frame, text="Cabal 200", command=lambda: self.domeo("200"))
        button2.pack(padx=20,pady=20)
        button3 = Button(self.frame, text="Apagar", command=lambda: self.apagar())
        button3.pack(padx=20,pady=20)'''
        
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)			
        return "break"
    
    def apagar_raspberry(self):
        result = tkMessageBox.askyesno("Apagar", "Vols apagar el PC ?")        #, icon='warning'
        if result == True:
            os.system("sudo halt")
        
		
    def domeo(self, opcio):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))			    
                    
            s.send(AUTENTICACIO.decode('hex'))
            time.sleep(1)
                        
            if (opcio == "60"):
                s.send(CABAL_60.decode('hex'))

            if (opcio == "120"):
                s.send(CABAL_120.decode('hex'))

            if (opcio == "bypass on"):
                s.send(BYPASS_ON.decode('hex'))

            if (opcio == "bypass off"):
                s.send(BYPASS_OFF.decode('hex'))            
				
            s.close()

            #res = subprocess.call(['iwgetid -r'],shell=True)
            #res = "*** " + subprocess.check_output(['iwgetid','-r']).replace('\n','').replace('r','') + " ***"
            #label_ssid.config(text=res)
            #SSID.set(res)
            #print(res)

        finally:
                print >> sys.stderr
                s.close()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        try:
            res = "[ " + subprocess.check_output(['iwgetid','-r']).replace('\n','').replace('r','') + " ]"
        except subprocess.CalledProcessError, e:
            res = "MODUL WIFI NO DETECTAT"
            
        #self.l_ssid.configure(text=res)
        self.canvas.itemconfig(self.l_ssid, text=res)
        self.tk.after(3000, self.update_clock)

         

'''
def wifi():
        t = threading.Timer(5.0, wifi)
        t.start()
        #print ("hello, world")
        #fo = open("ssid.txt", "r")
        #line = fo.readline()        
        #w.wifi_txt()
        print ("--")
'''        

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.toggle_fullscreen()
    w.update_clock()
    #t = threading.Timer(5.0, w.wifi_txt)
    #t = threading.Timer(5.0, wifi)
    #t.start()    
    w.tk.mainloop()
