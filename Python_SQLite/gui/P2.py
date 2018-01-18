#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0301, C0103, C0111, W0614, W0401
import sys
import json
import subprocess
import shlex
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk 
    from tkinter import *

import _header
import _footer
import Globals
#import f_countdown

class Pagina2(tk.Frame):
    """Pàgina 2"""

    segons_inici = 0
    segons_inici_referencia = 0
    rpm1_min = 0
    rpm1_max = 0
    rpm2_min = 0
    rpm2_max = 0

    prova1_ok = False
    prova2_ok = False
    prova3_ok = False

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        FILES = 6 #0,1,2,3,4
        COLUMNES = 6 #0,1,2,3
        self.grid_rowconfigure(0, weight=1)  #HEADER
        self.grid_rowconfigure(1, weight=1)  #ROWS COS PÀGINA
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)  #FOOTER

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)

        _header.header(self, COLUMNES, "1 - SENSE SENSOR %RH (OBTURACIÓ 0%)")

        self.cos_pagina()

        _footer.footer(self, controller, int(self.__class__.__name__[-1:]), FILES, COLUMNES, "")

        #subprocess.call(shlex.split('./test.sh param1 param2'))
        #subprocess.call("python script2.py 1", shell=True)                
        
        #self.after(3000, self.temporitzador)    #activo temporitzador

        #self.dades_prova_json() #carrego les dades de la prova (temps i ran    gs de valors)

    def temporitzador(self):
        if Globals.PAGINA_ACTUAL == "Pagina2":
            #self.v_rpm1.configure(text=datetime.datetime.now().time())
            #aux = read_holdings_inputs.funcio("010400000001")   #bloqueja bastant la GUI. Subprocess també bloqueja GUI.
            #p = subprocess.Popen("python ./utils/read_holdings_inputs.py 010400000001", stdout=subprocess.PIPE, shell=True)
            #out, err = p.communicate()
            try:
                file = open("./utils/holdings.txt", "r") #llegir del fitxer no bloqueja la GUI
                aux = file.readline()
                data = json.loads(aux)
                self.v_q_nominal.configure(text=data["H5"])
            except:
                print("Error json")

            try:
                file = open("./utils/inputs.txt", "r")
                aux = file.readline()
                data = json.loads(aux)
                self.v_q_70.configure(text=data["I2"])
                self.v_q_actual.configure(text=data["I4"])
                self.v_rpm1.configure(text=data["I6"])
                self.v_rpm2.configure(text=data["I7"])
            except:
                print("Error json")

        self.master.after(3000, self.temporitzador)     #executo cada 3 segons

    
    def countdown(self):
        """Necessari per a que es vagi cridant cada segon"""
        print("timer")
        #f_countdown.countdown(self, 5)    

    def resultat_final_prova(self):
        """Quan segons=0 comprova si els valors actuals estan dins del rang corresponent"""
        try:
            verd = PhotoImage(file='./imgs/green.png')
            vermell = PhotoImage(file='./imgs/red.png')
            if int(self.v_rpm1["text"]) >= self.rpm1_min and int(self.v_rpm1["text"]) <= self.rpm1_max:                
                self.label1.configure(image=verd)
                self.label1.image = verd
                self.prova1_ok = True
            else:
                self.label1.configure(image=vermell)
                self.label1.image = vermell
                self.prova1_ok = False

            if int(self.v_rpm2["text"]) >= self.rpm2_min and int(self.v_rpm2["text"]) <= self.rpm2_max:    
                self.label2.configure(image=verd)
                self.label2.image = verd
                self.prova2_ok = True
            else:
                self.label2.configure(image=vermell)
                self.label2.image = vermell
                self.prova2_ok = False

            if int(self.v_q_actual["text"]) == int(self.v_q_70["text"]):
                self.q_actual_pan.configure(image=verd)
                self.q_actual_pan.image = verd
                self.prova3_ok = True                
            else:
                self.q_actual_pan.configure(image=vermell)
                self.q_actual_pan.image = vermell
                self.prova3_ok = False

            self.segons.grid_forget()       #no l'amaga !?
            self.Boto_Countdown.grid()      #fer visible
            self.segons_inici = self.segons_inici_referencia    #restauro segons
            
            if self.prova1_ok == True and self.prova2_ok == True and self.prova3_ok == True:
                self.controller.show_frame("Pagina3")                
        except:
            print("Error resultat final")

    def cos_pagina(self):
        """Controls de la pàgina"""
        tk.Label(self, text='Q NOMINAL', borderwidth=1, font=('MS', 16, 'bold')).grid(row=1, column=0, columnspan=2)
        self.v_q_nominal = tk.Label(self, text='0', borderwidth=1, font=('MS', 16, 'bold'), fg="blue")
        self.v_q_nominal.grid(row=1, column=2, sticky="W")
        tk.Label(self, text='Q 70%', borderwidth=1, font=('MS', 16, 'bold')).grid(row=1, column=4)
        self.v_q_70 = tk.Label(self, text='0', borderwidth=1, font=('MS', 16, 'bold'), fg="blue")
        self.v_q_70.grid(row=1, column=5)

        tk.Label(self, text='Q ACTUAL', borderwidth=1, font=('MS', 16, 'bold')).grid(row=2, column=0, columnspan=2)
        gif1 = PhotoImage(file='./imgs/orange.png')
        self.v_q_actual = tk.Label(self, text='?', borderwidth=1, font=('MS', 16, 'bold'), fg="blue")
        self.v_q_actual.grid(row=2, column=2, sticky="W")      #he de separar el grid si vull poder configurar/editar el label
        self.q_actual_pan = tk.Label(self, image=gif1)
        self.q_actual_pan.image = gif1
        self.q_actual_pan.grid(row=2, column=3)   #sticky=NW

        tk.Label(self, text='RPM 1', borderwidth=1, font=('MS', 16, 'bold')).grid(row=3, column=0, columnspan=2)
        gif1 = PhotoImage(file='./imgs/orange.png')
        self.v_rpm1 = tk.Label(self, text='?', borderwidth=1, font=('MS', 16, 'bold'), fg="blue")
        self.v_rpm1.grid(row=3, column=2, sticky="W")      #he de separar el grid si vull poder configurar/editar el label
        self.label1 = tk.Label(self, image=gif1)
        self.label1.image = gif1
        self.label1.grid(row=3, column=3)   #sticky=NW
        self.rang_rpm1 = tk.Label(self, text='-', borderwidth=1, font=('MS', 16, 'bold'))
        self.rang_rpm1.grid(row=3, column=4, sticky="W") #, padx=(10, 100) padx=(left, right)

        tk.Label(self, text='RPM 2', borderwidth=1, font=('MS', 16, 'bold')).grid(row=4, column=0, columnspan=2)
        img2 = PhotoImage(file='./imgs/orange.png')
        self.v_rpm2 = tk.Label(self, text='?', borderwidth=1, font=('MS', 16, 'bold'), fg="blue")
        self.v_rpm2.grid(row=4, column=2, sticky="W")
        self.label2 = tk.Label(self, image=img2)
        self.label2.image = img2
        self.label2.grid(row=4, column=3)
        self.rang_rpm2 = tk.Label(self, text='-', borderwidth=1, font=('MS', 16, 'bold'))
        self.rang_rpm2.grid(row=4, column=4, sticky="W")
        
        #self.Boto_Countdown = tk.Button(self, text="ON", font=('MS', 24, 'bold'), bg="green", command=self.countdown)
        self.Boto_Countdown = tk.Button(self, text="ON", font=('MS', 24, 'bold'), bg="green", command=lambda:f_countdown.countdown(self, 5))
        self.Boto_Countdown.grid(row=5, column=3)

    def dades_prova_json(self):
        try:
            file = open("./dades_proves.txt", "r") #llegir del fitxer no bloqueja la GUI
            s = ""
            for line in file:
                s += line
            data = json.loads(s)
            self.segons_inici = int(data["P1_temps"])
            self.segons_inici_referencia = int(data["P1_temps"])
            self.rang_rpm1.configure(text="(" + str(data["P1_rpm1_min"]) + " - " + str(data["P1_rpm1_max"])+ ")")
            self.rang_rpm2.configure(text="(" + str(data["P1_rpm2_min"]) + " - " + str(data["P1_rpm2_max"])+ ")")

            self.rpm1_min = int(data["P1_rpm1_min"])
            self.rpm1_max = int(data["P1_rpm1_max"])
            self.rpm2_min = int(data["P1_rpm2_min"])
            self.rpm2_max = int(data["P1_rpm2_max"])
        except:
            print("Error json")
