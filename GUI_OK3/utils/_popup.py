#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk 
    from tkinter import *

def popupmsg(msg, width, height, color, mida_font, funcio):
    """Finestra de confirmació"""
    img_ok = PhotoImage(file="./imgs/ok.png")
    img_cancel = PhotoImage(file="./imgs/cancel.png")

    #popup = tk.Tk()
    popup = tk.Toplevel()   #per a la finestra modal
    popup.wm_title("Info")
    label = tk.Label(popup, text=msg, bg=color, font=("Helvetica", mida_font))
    label.pack(side="top", fill="x", pady=20)
    but1 = tk.Button(popup, image=img_ok, relief=FLAT, bg=color, highlightcolor=color,
                     activebackground=color, bd=0, highlightthickness=0, command=lambda: eval(funcio))
    but1.image = img_ok
    but1.pack(side=LEFT, padx=10)
    but2 = tk.Button(popup, image=img_cancel, relief=FLAT, bg=color, highlightcolor=color,
                     activebackground=color, bd=0, highlightthickness=0, command=popup.destroy)
    but2.image = img_cancel
    but2.pack(side=RIGHT, padx=10)
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    posx = (screen_width/2) - (width/2)
    posy = (screen_height/2) - (height/2)
    popup.geometry('%dx%d+%d+%d' % (width, height, posx, posy))
    popup.overrideredirect(1) #Remove border
    popup.configure(background=color)
    popup.mainloop()
