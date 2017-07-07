from tkinter import *

from Globals import raise_frame
from header import header_

def pagina(f1,f2):
    header_(f1)
    Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
    Label(f1, text='FRAME 1').pack()
    f1.after(1000, temporitzador)

def temporitzador():
    print("***")    