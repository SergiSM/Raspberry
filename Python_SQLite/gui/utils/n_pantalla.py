#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import Globals
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk 
    from tkinter import *

def popupmsg(controller, width, height, color, mida_font, funcio):
    """Finestra de confirmaci�"""

    Globals.POP_UP_NUM_ON = True    #aviso de que s'ha aixecat pop up per saltar de pantalla

    img_ok = PhotoImage(file="./imgs/ok.png")
    img_cancel = PhotoImage(file="./imgs/cancel.png")

    #popup = tk.Tk()
    popup = tk.Toplevel()   #per a la finestra modal
    popup.wm_title("Info")

    b1 = tk.Button(popup, text="1", font=('MS', 40, 'bold'), bg="green", command=lambda:saltar_pantalla(popup, controller, "Pagina2"))
    b1.pack(side=LEFT, padx=10)
    b2 = tk.Button(popup, text="2", font=('MS', 40, 'bold'), bg="green", command=lambda:saltar_pantalla(popup, controller, "Pagina3"))
    b2.pack(side=LEFT, padx=10)
    b3 = tk.Button(popup, text="3", font=('MS', 40, 'bold'), bg="green", command=lambda:saltar_pantalla(popup, controller, "Pagina4"))
    b3.pack(side=LEFT, padx=10)
    b4 = tk.Button(popup, text="4", font=('MS', 40, 'bold'), bg="green", command=lambda:saltar_pantalla(popup, controller, "Pagina5"))
    b4.pack(side=LEFT, padx=10)
    b5 = tk.Button(popup, text="5", font=('MS', 40, 'bold'), bg="green", command=lambda:saltar_pantalla(popup, controller, "Pagina6"))
    b5.pack(side=LEFT, padx=10)
    b6 = tk.Button(popup, text="6", font=('MS', 40, 'bold'), bg="green", command=lambda:saltar_pantalla(popup, controller, "Pagina7"))
    b6.pack(side=LEFT, padx=10)
    b7 = tk.Button(popup, text="7", font=('MS', 40, 'bold'), bg="green", command=lambda:saltar_pantalla(popup, controller, "Pagina8"))
    b7.pack(side=LEFT, padx=10)

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    posx = (screen_width/2) - (width/2)
    posy = (screen_height/2) - (height/2)
    popup.geometry('%dx%d+%d+%d' % (width, height, posx, posy))
    popup.overrideredirect(1) #Remove border
    popup.configure(background=color)
    popup.mainloop()

def saltar_pantalla(popup, controller, pagina):
    popup.destroy()

    #SEGONS PANTALLA, FER EL CANVI DE VELOCITAT -> CREAR FITXER canvi_velocitat.txt amb 40, 80 o 120
    

    controller.show_frame(pagina)
    Globals.POP_UP_NUM_ON = False
