#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk 
    from tkinter import *

def footer(frame, controller, n_pag, n_row):
    "Peu de la pàgina"
    img_next = PhotoImage(file="./imgs/next.png")
    img_prev = PhotoImage(file="./imgs/prev.png")
    
    if n_pag > 1:
        but = tk.Button(frame, image=img_prev, relief=FLAT, command=lambda:
                        controller.show_frame("Pagina"+str(n_pag-1)))
        but.image = img_prev
        but.grid(row=n_row, column=0, sticky="w", padx=5, pady=5)
        frame.columnconfigure(0, weight=1)

    if controller.TOTAL_PAGINES >= (n_pag+1):
        but = tk.Button(frame, image=img_next, relief=FLAT, command=lambda:
                        controller.show_frame("Pagina"+str(n_pag+1)))
        but.image = img_next
        but.grid(row=n_row, column=2, sticky="e", padx=5, pady=5)   #e = align right
        frame.columnconfigure(2, weight=1)
