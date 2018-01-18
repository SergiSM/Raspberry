
import sys
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
import Globals