from tkinter import *
from Globals import raise_frame
import p1
import p2

root = Tk()

f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')

p1.pagina(f1,f2)
p2.pagina(f2,f1)

raise_frame(f1)
root.mainloop()