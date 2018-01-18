#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import _popup

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk
    from tkinter import *

def header(frame, n_cols, titol):
    """Capçalera de la pàgina"""
    img_shutdown = PhotoImage(file="./imgs/shutdown.png")
    img_close = PhotoImage(file="./imgs/close.png")

    but2 = tk.Button(frame, image=img_close, relief=FLAT, command=lambda: _popup.popupmsg("Vols tancar l'aplicació ?", 400, 300, '#1E90FF', 20,"sys.exit()"))    
    but2.image = img_close
    but2.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    but3 = tk.Button(frame, image=img_close, relief=FLAT, command=lambda: _popup.popupmsg("Vols tancar l'aplicació ?", 400, 300, '#1E90FF', 20,"sys.exit()"))    
    but3.image = img_close
    but3.grid(row=0, column=1, sticky="nw", padx=5, pady=5)
    #but2.grid(row=0, column=n_cols, sticky="ne", padx=5, pady=5)

    '''    
    but1 = tk.Button(frame, image=img_shutdown, relief=FLAT, command=lambda:
                     _popup.popupmsg("Vols apagar el PC ?", 400, 300, '#1E90FF', 20,
                                     "os.system('sudo shutdown now -h')"))
    but1.image = img_shutdown
    but1.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    frame.columnconfigure(0, weight=1)
    if titol != "":
        lab1 = tk.Label(frame, text=titol, font=('MS', 15, 'bold'), bg="orange")
        lab1.grid(row=0, column=1, sticky="news", padx=10, pady=0, columnspan=n_cols - 2)   #el títol ocupa tot l'espai menys els troços dels extrems
    frame.columnconfigure(1, weight=1)
    
    #but2 = tk.Button(frame, image=img_close, relief=FLAT, command=lambda: _popup.popupmsg("Vols tancar l'aplicació ?", 400, 300, '#1E90FF', 20,"sys.exit()"))    
    #but2.image = img_close
    but2 = tk.Label(frame, text="")
    but2.grid(row=0, column=n_cols, sticky="ne", padx=5, pady=5)   #ocupa l'última columna
    frame.columnconfigure(2, weight=1)'''
