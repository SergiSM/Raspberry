#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
else:
    import tkinter as tk

import P1

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes("-fullscreen", True)  

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        frame = P1.Pagina1(parent=container, controller=self)            
        frame.config(background='black')
        frame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()