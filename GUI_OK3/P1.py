#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import _header
import _footer
import _popup
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk
    from tkinter import *

class Pagina1(tk.Frame):
    """Pàgina 1"""
    ultim_row = 0   #després de crear el cos de la pàgina, aquesta variable indica el row del footer
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        _header.header(self)

        self.cos_pagina()

        _footer.footer(self, controller, int(self.__class__.__name__[-1:]), self.ultim_row+1)
        #int(self.__class__.__name__[-1:]) Obtinc el número de pàgina (Pagina1 -> 1)

    def cos_pagina(self):
        """Controls de la pàgina"""
        lab1 = tk.Label(self, text="PÀGINA 1")
        lab1.grid(row=1, columnspan=3, sticky="news")
        self.rowconfigure(1, weight=1)
        lab2 = tk.Button(self, text="*****", command=lambda:self.modificar_label(lab1))
        lab2.grid(row=2, columnspan=1, sticky="news")
        self.rowconfigure(1, weight=1)
        lab3 = tk.Label(self, text="PÀGINA 1")
        lab3.grid(row=3, columnspan=3, sticky="news")
        self.rowconfigure(1, weight=1)
        lab4 = tk.Label(self, text="PÀGINA 1")
        lab4.grid(row=4, columnspan=3, sticky="news")
        self.rowconfigure(1, weight=1)
        self.ultim_row = 4

    def modificar_label(self, label):        
        label.configure(text=label["text"]+"*")
        