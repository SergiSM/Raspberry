#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from functools import partial

root = tkinter.Tk()
root.geometry('800x480')

def clic(digit):    
    print(digit)

o_px = 30
px = o_px
py = 40

columna = 0
fila = 1
for i in range(1,11):
    t = tkinter.Button(root, width=4, height=3, text=str(i), bg="silver", font=('MS', 30, 'bold'), command=partial(clic, str(i)))    

    if i == 6:
        columna=0
        fila=2

    t.grid(row=fila,column=columna, sticky='EWNS')
    root.grid_columnconfigure(columna, weight=1)
    root.grid_rowconfigure(fila, weight=1)
    columna = columna + 1

root.mainloop()

'''t.place(x=px, y=py)
    px = px + 120
    if i == 5:
        px = o_px
        py = py + 200'''
