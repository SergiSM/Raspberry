#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import _header
import _footer
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk
    from tkinter import *

class Pagina3(tk.Frame):
    """Pàgina 3"""
    ultim_row = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        _header.header(self)

        self.cos_pagina()

        _footer.footer(self, controller, int(self.__class__.__name__[-1:]), self.ultim_row+1)

    def cos_pagina(self):
        """Controls de la pàgina"""
        lab = tk.Label(self, text="PÀGINA 3")
        lab.grid(row=1, columnspan=3, sticky="news")
        self.rowconfigure(1, weight=1)
        self.ultim_row = 1
