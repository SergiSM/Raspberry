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
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
else:
    import tkinter as tk

class SampleApp(tk.Tk):
    """Python GUI"""
    TOTAL_PAGINES = 4   #nombre total de pàgines de l'aplicació

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes("-fullscreen", True)    #self.wm_state("zoomed") #maximitzat

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for frms in (P1.Pagina1, P2.Pagina2, P3.Pagina3, P4.Pagina4):       #guardo totes les pàgines(classes)
            page_name = frms.__name__
            frame = frms(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Pagina1")  #primera pàgina a obrir-se

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
