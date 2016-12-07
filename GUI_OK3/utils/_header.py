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

def header(frame):
    """Capçalera de la pàgina"""
    img_shutdown = PhotoImage(file="./imgs/shutdown.png")
    img_close = PhotoImage(file="./imgs/close.png")

    but1 = tk.Button(frame, image=img_shutdown, relief=FLAT, command=lambda:
                     _popup.popupmsg("Vols apagar el PC ?", 400, 300, '#1E90FF', 20,
                                     "os.system('sudo shutdown now -h')"))
    but1.image = img_shutdown
    but1.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    frame.columnconfigure(0, weight=1)
    lab1 = tk.Label(frame, text="PÀGINA 1")
    lab1.grid(row=0, column=1, sticky="news", padx=5, pady=5)
    frame.columnconfigure(1, weight=1)
    but2 = tk.Button(frame, image=img_close, relief=FLAT, command=lambda:
                     _popup.popupmsg("Vols tancar l'aplicació ?", 400, 300, '#1E90FF', 20,
                                     "sys.exit()"))
    but2.image = img_close
    but2.grid(row=0, column=2, sticky="e", padx=5, pady=5)
    frame.columnconfigure(2, weight=1)

