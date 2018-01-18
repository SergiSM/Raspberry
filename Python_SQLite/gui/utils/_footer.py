#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import n_pantalla
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk 
    from tkinter import *

def footer(frame, controller, n_pag, n_row, n_columnes, extra):
    "Peu de la pàgina"
    img_next = PhotoImage(file="./imgs/next.png")
    img_prev = PhotoImage(file="./imgs/prev.png")
   
    '''if n_pag > 2:
        but = tk.Button(frame, image=img_prev, relief=FLAT, command=lambda:
                        controller.show_frame("Pagina"+str(n_pag-1)))
        but.image = img_prev
        but.grid(row=n_row, column=0, sticky="ws", padx=5, pady=5)
        frame.columnconfigure(0, weight=1)

    if controller.TOTAL_PAGINES >= (n_pag+1):
        but = tk.Button(frame, image=img_next, relief=FLAT, command=lambda:
                        controller.show_frame("Pagina"+str(n_pag+1)))
        but.image = img_next
        but.grid(row=n_row, column=n_columnes, sticky="es", padx=5, pady=5)   #e = align right, columna de més a la dreta
        frame.columnconfigure(2, weight=1)'''

    if n_pag > 1:
        img_numbers = PhotoImage(file="./imgs/numbers.png")
        b_num = tk.Button(frame, image=img_numbers, relief=FLAT, command=lambda:n_pantalla.popupmsg(controller, 600, 200, '#000000', 20, ""))        
        b_num.image = img_numbers
        b_num.grid(row=n_row, column=0)

    #if extra == "NO NEXT":  #trec el botó de next
    #    but.grid_remove()
    