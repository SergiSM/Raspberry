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

class Pagina1(tk.Frame):  
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
        self.controller = controller    #per canviar de pantalla
        self.estructura()

        #self.after(1000, self.temporitzador) 

    def estructura(self):
        
        #TOP
        top_frame = Frame(self, bg='#568ed8', height=50)
        top_frame.grid(row=0, sticky="ew", columnspan=8)  #columnspan=2 perque panell de sota t� 2 c�l�les | ew = cobreix tot ample pantalla (width), el height �s fixe = 50        

        #CENTER   
        FONT = 14     

        #0
        llista_c = []
        row = 1     #no treure !
        col = 0
        colors = ['silver', '#cccccc']
        for i in range(1, 14):
            c1 = Frame(self, bg=colors[i % 2], padx=0, pady=0)
            c1.grid(row=row, column=col, sticky="news", padx=(0,2), pady=(0,2))            
            llista_c.append(c1)
            row=row+1 

        r = 1
        hh = ["08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "17:00 - 18:00", "18:00 - 19:00", "19:00 - 20:00"]        
        for h in hh: 
            lab = tk.Label(llista_c[r-1], text=h, font=('MS', FONT, 'bold'), fg="black", bg=colors[r % 2])
            lab.grid(row=r, column=0, padx=(30,0), pady=(20,0))    #, padx=(0,0), pady=(0,0)
            r = r + 1

        #1
        llista_c = []
        row = 1     #no treure !
        col = 1
        colors = ['silver', 'blue', 'green']
        text = ['0', 'A', 'Assig3']
        amples = [1, 2, 3]
        i = 0
        for ample in amples:
            c1 = Frame(self, bg=colors[i], padx=0, pady=0)
            c1.grid(row=row, column=col, sticky="news", rowspan=ample, padx=(0,2), pady=(0,2))
            llista_c.append(c1)

            #len=16 -> padx=0    
            aux_padx = len(text[i])
            lab = tk.Label(c1, text=text[i], font=('MS', FONT, 'bold'), fg="black", bg=colors[i])
            lab.grid(row=r, column=0, padx=(40,0), pady=(20*ample,0))
            row=row+ample
            i = i+1 

        #2
        row = 1  #no treure !
        col = 2
        colors = ['silver', 'blue', 'green']
        amples = [3, 2, 1]
        i = 0
        for ample in amples:
            c1 = Frame(self, bg=colors[i], padx=0, pady=0)
            c1.grid(row=row, column=col, sticky="news", rowspan=ample, padx=(0,2), pady=(0,2))
            lab = tk.Label(c1, text=text[i], font=('MS', FONT, 'bold'), fg="black", bg=colors[i])
            lab.grid(row=r, column=0)
            row=row+ample
            i = i+1  

        #3
        row = 1
        col = 3
        colors = ['silver', 'blue', 'green']
        amples = [6, 2, 1]
        i = 0
        for ample in amples:
            c1 = Frame(self, bg=colors[i], padx=0, pady=0)
            c1.grid(row=row, column=col, sticky="news", rowspan=ample, padx=(0,2), pady=(0,2))
            lab = tk.Label(c1, text=text[i], font=('MS', FONT, 'bold'), fg="black", bg=colors[i])
            lab.grid(row=r, column=0)
            row=row+ample
            i = i+1   

        #4
        row = 1
        col = 4
        colors = ['silver', 'red', 'green']
        amples = [1, 2, 4]
        i = 0
        for ample in amples:
            c1 = Frame(self, bg=colors[i], padx=0, pady=0)
            c1.grid(row=row, column=col, sticky="news", rowspan=ample, padx=(0,2), pady=(0,2))
            lab = tk.Label(c1, text=text[i], font=('MS', FONT, 'bold'), fg="black", bg=colors[i])
            lab.grid(row=r, column=0)
            row=row+ample
            i = i+1  

        #5
        row = 1
        col = 5
        colors = ['yellow', 'red', 'green']
        amples = [4, 1, 3]
        i = 0
        for ample in amples:
            c1 = Frame(self, bg=colors[i], padx=0, pady=0)
            c1.grid(row=row, column=col, sticky="news", rowspan=ample, padx=(0,2), pady=(0,2))
            lab = tk.Label(c1, text=text[i], font=('MS', FONT, 'bold'), fg="black", bg=colors[i])
            lab.grid(row=r, column=0)
            row=row+ample
            i = i+1 

        #6
        row = 1
        col = 6
        colors = ['yellow', 'red', 'green']
        amples = [1, 1, 3]
        i = 0
        for ample in amples:
            c1 = Frame(self, bg=colors[i], padx=0, pady=0)
            c1.grid(row=row, column=col, sticky="news", rowspan=ample, padx=(0,2), pady=(0,2))
            lab = tk.Label(c1, text=text[i], font=('MS', FONT, 'bold'), fg="black", bg=colors[i])
            lab.grid(row=r, column=0)
            row=row+ample
            i = i+1

        #7
        row = 1
        col = 7
        colors = ['yellow', 'red', 'green']
        amples = [4, 1, 3]
        i = 0
        for ample in amples:
            c1 = Frame(self, bg=colors[i], padx=0, pady=0)
            c1.grid(row=row, column=col, sticky="news", rowspan=ample, padx=(0,2), pady=(0,2))
            lab = tk.Label(c1, text=text[i], font=('MS', FONT, 'bold'), fg="black", bg=colors[i])
            lab.grid(row=r, column=0)
            row=row+ample
            i = i+1

        for r in range(1,14):
            self.grid_rowconfigure(r, weight=1)            

        for r in range(8):            
            self.grid_columnconfigure(r, weight=1)

        '''c1 = Frame(self, bg='white', padx=0, pady=0)
        c1.grid(row=1, column=0, sticky="news") #ew = cobreix tot ample pantalla, ns = cobreix tot alt pantalla (de la disponible segons els altres frames)
        
        center_frame2 = Frame(self, bg='orange', padx=0, pady=0)
        center_frame2.grid(row=1, column=1, sticky="news")   

        center_frame3 = Frame(self, bg='white', padx=0, pady=0)
        center_frame3.grid(row=1, column=2, sticky="news")   

        center_frame4 = Frame(self, bg='orange', padx=0, pady=0)
        center_frame4.grid(row=1, column=3, sticky="news")    

        center_frame5 = Frame(self, bg='white', padx=0, pady=0)
        center_frame5.grid(row=1, column=4, sticky="news")   

        center_frame6 = Frame(self, bg='orange', padx=0, pady=0)
        center_frame6.grid(row=1, column=5, sticky="news") 

        center_frame7 = Frame(self, bg='white', padx=0, pady=0)
        center_frame7.grid(row=1, column=6, sticky="news")   

        lab = tk.Label(c1, text="Vdffsdfsd", font=('MS', FONT, 'bold'), fg="black", bg="#568ed8")
        lab.grid(row=0, column=0, padx=(0,0), pady=(0,0))'''
        
        #TOOLBAR - TOP CONTROLS
        #toolbar.crear(self, top_frame, 2)   #2 per a que botó logo faci saltar a Pàgina 2

        #p1_lectures.display(self, center_frame1)

        #p1_tecles_accions.crear_tecles(self, center_frame2)        

        #GRID CONFIGURE
        '''self.grid_rowconfigure(1, weight=1) # com que la columna 1 no t� definit el height perque s'ajusta autom�ticament sticky="news", llavors cal especificar el weight
                                            # com que les columnes 0 i 2 del top_frame i del btm_frame tenen un height fixe, i nom�s ajustem horitzontalment (sticky="ew"), llavors
                                            # no cal especificar el grid_rowconfigure de les columnes 0 i 2
        
        
        self.grid_columnconfigure(0, weight=14) 
        self.grid_columnconfigure(1, weight=14) 
        self.grid_columnconfigure(2, weight=14) 
        self.grid_columnconfigure(3, weight=14) 
        self.grid_columnconfigure(4, weight=14) 
        self.grid_columnconfigure(5, weight=14) 
        self.grid_columnconfigure(6, weight=14) '''

    def temporitzador(self):        
        '''self.hora["text"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")        
        self.PAS = self.PAS + 1'''

        self.after(1000, self.temporitzador)