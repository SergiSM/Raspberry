#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''import sys
import _header
import _footer
import _popup
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
    import ttk
else:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk
import sqlite3 as lite  
import toolbar
import Globals'''
from imports_pagines import *   #no recomanable

class Pagina1(tk.Frame):
    """Pàgina 1"""
    con = lite.connect(Globals.RUTA_BBDD)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
        self.controller = controller    #per canviar de pantalla
        self.estructura()                               

    def estructura(self):
        # create all of the main containers
        top_frame = Frame(self, bg='silver', width=450, height=50)
        center = Frame(self, bg='gray2', width=50, height=40, padx=3, pady=3)
        btm_frame = Frame(self, bg='white', width=450, height=45)        

        # layout all of the main containers
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=2, sticky="ew")

        #TOOLBAR        
        toolbar.crear(self, top_frame)

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_rowconfigure(1, weight=4)
        center.grid_columnconfigure(0, weight=1)

        ctr_search = Frame(center, bg='silver', width=100, height=190)
        ctr_result = Frame(center, bg='orange', width=250, height=190, padx=3, pady=3)        

        ctr_search.grid(row=0, column=0, sticky="nwse")   #sticky="nwse" nw = des de dalt(n) a l'esquerra(w), se = expandir fins a baix(s) a la dreta(e)
        ctr_result.grid(row=1, column=0, sticky="nwse")

        #SEARCH
        self.search_word = tk.Entry(ctr_search, font=('MS', 10, 'bold')) #no poso el grid aquí perque llavors no puc accedira objecte (area_text.insert falla)
        self.search_word.grid(row=0, column=0, sticky=NE, padx = 10)  
        search_button = tk.Button(ctr_search, text="Buscar", bg="green", font=('MS', 8, 'bold'), command=self.search_button_click)
        search_button.grid(row=0, column=1, sticky=NW)

        self.combo_team = ttk.Combobox(ctr_search, textvariable="", state="readonly")        
        x = []
        with self.con:    
            cur = self.con.cursor() 
            cur.execute("SELECT DISTINCT(team) FROM players ORDER BY team") 
            rows = cur.fetchall()        
            for row in rows:
                x.append(row[0])
        self.combo_team["values"] = x       #self.combo_team["values"] = ["Python", "C", "C++", "Java"]        
        self.combo_team.bind("<<ComboboxSelected>>", self.selection_changed)
        self.combo_team.grid(row=0, column=2)
        
        #RESULT
        self.area_text = tk.Text(ctr_result, font=('MS', 10, 'bold'), borderwidth=1, relief="sunken") #no poso el grid aquí perque llavors no puc accedira objecte (area_text.insert falla)                        
        vsb = tk.Scrollbar(ctr_result, orient="vertical", command=self.area_text.yview)                
        vsb.grid(row=3, column=2, sticky='nsew')
        self.area_text.grid(row=3, column=1, sticky="NEWS")  #amb les cometes "" expandeixo en totes direccions N E W S

        self.dades_sqlite("")

    def dades_sqlite(self, word_to_search):
        """Realitzar consulta SQL i ho mostra a area_text"""
        self.area_text.delete('1.0', END)       #borrar text area             
        with self.con:    
            cur = self.con.cursor() 
            cur.execute("SELECT name, team FROM players WHERE team LIKE '%" + word_to_search + "%'") 
            rows = cur.fetchall()        
            for row in rows:                
                self.area_text.insert(INSERT, str(row)+"\n")

    def search_button_click(self):
        """Botó buscar"""        
        self.dades_sqlite(self.search_word.get())  

    def selection_changed(self, event):           
        """Combo on change"""
        self.dades_sqlite(self.combo_team.get())  

    