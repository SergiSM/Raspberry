#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import sys
import os
import sqlite3 as lite
from funcions import uprint
    

con = lite.connect('D:\PROJECTES_2\python_excel\data.s3db')

book = xlrd.open_workbook(os.path.dirname(__file__) + "\\" + sys.argv[1])
sh = book.sheet_by_index(0)

with con:
    
    cur = con.cursor() 
    for rx in range(1,sh.nrows):    #descarto primer linea
        title = sh.cell_value(rowx=rx, colx=4).replace("'","''")

        if titulo != "":
            cur.execute("SELECT COUNT(*) FROM films WHERE title = ?", (titulo,))
            data=cur.fetchone()[0]
            if data==0:
                cur.execute("INSERT INTO films (title) VALUES ('"+title+"')")