#!/usr/bin/env python
# -*- coding: utf-8 -*-
from imports_pagines import *   #no recomanable

class Pagina7(tk.Frame):  

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
        self.controller = controller    #per canviar de pantalla
        self.estructura() 

    def estructura(self):
        #TOP
        top_frame = Frame(self, bg='silver', height=50)
        top_frame.grid(row=0, sticky="ew", columnspan=2)  #columnspan=2 perque panell de sota té 2 cèl·les | ew = cobreix tot ample pantalla (width), el height és fixe = 50
        
        #CENTER
        center_frame0 = Frame(self, bg='yellow', padx=3, pady=3, height=100)
        center_frame0.grid(row=1, column=0, sticky="ew", columnspan=2)

        center_frame1 = Frame(self, bg='blue', padx=3, pady=3)
        center_frame1.grid(row=2, column=0, sticky="news") #ew = cobreix tot ample pantalla, ns = cobreix tot alt pantalla (de la disponible segons els altres frames)
        
        center_frame2 = Frame(self, bg='cyan', padx=3, pady=3)
        center_frame2.grid(row=2, column=1, sticky="news")

        #BOTTOM
        btm_frame = Frame(self, bg='orange', height=30)
        btm_frame.grid(row=3, sticky="ew", columnspan=2)  #ew = cobreix tot ample pantalla (width), el height és fixe = 30
        
        #GRID CONFIGURE        
        self.grid_rowconfigure(2, weight=1)     #només ajusto aquesta fila perque és la que s'ajusta automàticament -> sticky="news"
                                                #les altres al tenir un height i sticky="ew", no cal fer grid_rowconfigure
        
        self.grid_columnconfigure(0, weight=1) # 33% com que hi ha 2 columnes, assigno a la de la dreta el doble de width que la de l'esquerra
        self.grid_columnconfigure(1, weight=2) # 66%        

        #TOOLBAR - TOP CONTROLS
        toolbar.crear(self, top_frame)

        #BOTTOM CONTROLS
        self.controls(btm_frame)

        self.data(center_frame1)

    def controls(self, frame):
        c1 = tk.Button(frame, text="OK", bg="green", relief=FLAT, command=lambda: self.controller.show_frame("Pagina1"))
        c1.grid(row=0, column=0, padx=5)

    def data(self, frame):
        self.dia = tk.Label(frame, text="1", font=('MS', 32, 'bold'))
        self.dia.grid(row=1, column=0, padx=20)

        c1 = tk.Button(frame, text="+", bg="green", relief=FLAT, command=lambda: self.inc_label(self.dia, "dia"))
        c1.grid(row=0, column=0, padx=5)        

        c2 = tk.Button(frame, text="-", bg="green", relief=FLAT, command=lambda: self.controller.show_frame("Pagina1"))
        c2.grid(row=2, column=0, padx=5)

        self.mes = tk.Label(frame, text="1", font=('MS', 32, 'bold'))
        self.mes.grid(row=1, column=1, padx=20)

        c1 = tk.Button(frame, text="+", bg="green", relief=FLAT, command=lambda: self.inc_label(self.mes, "mes"))
        c1.grid(row=0, column=1, padx=5)        

        c2 = tk.Button(frame, text="-", bg="green", relief=FLAT, command=lambda: self.controller.show_frame("Pagina1"))
        c2.grid(row=2, column=1, padx=5)

    def inc_label(self, label, tipus):
        
        label["text"] = int(label["text"]) + 1

        if ((tipus == "dia") and (int(label["text"]) == 32)):
            label["text"] = "1"                    
        
        if ((tipus == "mes") and (int(label["text"]) == 13)):
            label["text"] = "1"
            
        print(label.cget("text"))
        print(label)
        #self.dia["text"] = int(self.dia["text"]) + 1
        
        