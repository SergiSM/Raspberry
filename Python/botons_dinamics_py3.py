#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from functools import partial

def clic(ruta): 
    print(ruta)

root = tkinter.Tk()

cont = 0
columna = 0
fila = 1
for i in range(1,10):
    t = tkinter.Button(root, width=4, height=3, text=str(i), bg="green", font=('MS', 30, 'bold'), command=partial(clic, str(i)))
    t.grid(row=fila,column=columna, sticky='EWNS')
    root.grid_columnconfigure(columna, weight=1)
    root.grid_rowconfigure(fila, weight=1)
    fila = fila + 1
    cont = cont + 1

root.mainloop()
