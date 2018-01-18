#!/usr/bin/env python
# -*- coding: utf-8 -*-
from imports_pagines import *   #no recomanable

class Pagina5(tk.Frame):  

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
        self.controller = controller    #per canviar de pantalla
        self.estructura() 

    def estructura(self):
        #TOP
        top_frame = Frame(self, bg='silver', height=50)
        top_frame.grid(row=0, sticky="ew", columnspan=2)  #columnspan=2 perque panell de sota té 2 cèl·les | ew = cobreix tot ample pantalla (width), el height és fixe = 50
        
        #CENTER
        center_frame1 = Frame(self, bg='blue', padx=3, pady=3)
        center_frame1.grid(row=1, column=0, sticky="news") #ew = cobreix tot ample pantalla, ns = cobreix tot alt pantalla (de la disponible segons els altres frames)
        
        center_frame2 = Frame(self, bg='cyan', padx=3, pady=3)
        center_frame2.grid(row=1, column=1, sticky="news")

        #BOTTOM
        btm_frame = Frame(self, bg='orange', height=30)
        btm_frame.grid(row=2, sticky="ew", columnspan=2)  #ew = cobreix tot ample pantalla (width), el height és fixe = 30
        
        #GRID CONFIGURE
        self.grid_rowconfigure(1, weight=1) # com que la columna 1 no té definit el heigh perque s'ajusta automàticament sticky="news", llavors cal especificar el weight
                                            # com que les columnes 0 i 2 del top_frame i del btm_frame tenen un height fixe, i només ajustem horitzontalment (sticky="ew"), llavors
                                            # no cal especificar el grid_rowconfigure de les columnes 0 i 2

        #self.grid_columnconfigure(0, weight=1) #com que hi ha 2 columnes, assigno el mateix espai a cadascuna
        #self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1) # 33% com que hi ha 2 columnes, assigno a la de la dreta el doble de width que la de l'esquerra
        self.grid_columnconfigure(1, weight=2) # 66%        

        #TOOLBAR - TOP CONTROLS
        toolbar.crear(self, top_frame)

        #BOTTOM CONTROLS
        self.controls(btm_frame)

    def controls(self, frame):
        c1 = tk.Button(frame, text="OK", bg="green", relief=FLAT, command=lambda: self.controller.show_frame("Pagina1"))
        c1.grid(row=0, column=0, padx=5)
        
