#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
import sys
if platform.system() == "Windows":
    sys.path.insert(0, sys.path[0]+'\\utils')   #ruta a llibreria
else:
    sys.path.insert(0, sys.path[0]+'/utils')
import P1   #pàgines de l'aplicació
import P2
import P3
import P4
import P5
import P6
import P7
import Globals

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
else:
    import tkinter as tk

#call python multifinestra.py instead of python PATH/multifinestra.py
class SampleApp(tk.Tk):    
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.attributes("-fullscreen", True)  
        if platform.system() == "Windows":   
            self.wm_state("zoomed") #maximitzat

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}        
        for frms in (P1.Pagina1, P2.Pagina2, P3.Pagina3, P4.Pagina4, P5.Pagina5, P6.Pagina6, P7.Pagina7):       #guardo totes les pàgines(classes)
            page_name = frms.__name__
            frame = frms(parent=container, controller=self)            
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Pagina1")  #primera pàgina a obrir-se

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()
                
        try:            
            frame.label0["text"] = ""   #puc editar controls si existeixen en el frame carregat (try ...)
        except:
            pass        

        Globals.PAGINA_ACTUAL = page_name

if __name__ == "__main__":
    app = SampleApp()
    if platform.system() == "Windows":
        app.iconbitmap(r'C:\Users\externo101\Documents\PROVES_SERGI\Python_SQLite\gui\database.ico')
    app.mainloop()
