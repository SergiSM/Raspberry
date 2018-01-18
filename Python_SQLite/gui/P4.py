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

import toolbar
import utils_frames
import Globals

class Pagina4(tk.Frame):  

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
        self.controller = controller    #per canviar de pantalla
        self.estructura() 

    def estructura(self):
        # create all of the main containers
        top_frame = Frame(self, bg='silver', height=50)
        top_frame.grid(row=0, sticky="ew")  #ew = cobreix tot ample pantalla (width), el height és fixe = 50
        
        center_frame = Frame(self, bg='blue', padx=3, pady=3)
        center_frame.grid(row=1, sticky="nsew") #ew = cobreix tot ample pantalla, ns = cobreix tot alt pantalla (de la disponible segons els altres frames)
        
        btm_frame = Frame(self, bg='white', height=30)
        btm_frame.grid(row=2, sticky="ew")  #ew = cobreix tot ample pantalla (width), el height és fixe = 30
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        toolbar.crear(self, top_frame)