from tkinter import *

from Globals import raise_frame
from header import header_

def pagina(f2,f1):
    header_(f2)
    Label(f2, text='FRAME 2').pack()
    Button(f2, text='Go to frame 1', command=lambda:raise_frame(f1)).pack()
