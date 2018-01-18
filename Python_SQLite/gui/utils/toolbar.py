#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
    import ttk
else:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk

def crear(self, frame):
    img_close = PhotoImage(file="./imgs/close.png")

    but1 = tk.Button(frame, image=img_close, bg="silver", relief=FLAT, command=lambda: self.controller.show_frame("Pagina1"))
    but1.image = img_close
    but1.grid(row=0, column=0, sticky="nw")

    but2 = tk.Button(frame, image=img_close, bg="silver", relief=FLAT, command=lambda: self.controller.show_frame("Pagina2"))
    but2.image = img_close
    but2.grid(row=0, column=1, sticky="nw", padx=0, pady=0)   

    but3 = tk.Button(frame, image=img_close, bg="silver", relief=FLAT, command=lambda: self.controller.show_frame("Pagina3"))
    but3.image = img_close
    but3.grid(row=0, column=2, sticky="nw")

    but4 = tk.Button(frame, image=img_close, bg="silver", relief=FLAT, command=lambda: self.controller.show_frame("Pagina4"))
    but4.image = img_close
    but4.grid(row=0, column=3, sticky="nw")

    but5 = tk.Button(frame, image=img_close, bg="silver", relief=FLAT, command=lambda: self.controller.show_frame("Pagina5"))
    but5.image = img_close
    but5.grid(row=0, column=4, sticky="nw")
   
    but6 = tk.Button(frame, image=img_close, bg="silver", relief=FLAT, command=lambda: self.controller.show_frame("Pagina6"))
    but6image = img_close
    but6.grid(row=0, column=5, sticky="nw")

    but7 = tk.Button(frame, image=img_close, bg="silver", relief=FLAT, command=lambda: self.controller.show_frame("Pagina7"))
    but7image = img_close
    but7.grid(row=0, column=6, sticky="nw")
    