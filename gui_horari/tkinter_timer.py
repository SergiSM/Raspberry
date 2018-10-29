#!/usr/bin/python

import tkinter
root = tkinter.Tk()

def update_clock():
    root.after(1000, update_clock)
    print("*")

root.after(1000, update_clock)
root.mainloop()
