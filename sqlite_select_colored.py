#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import sys
from funcions import uprint
from termcolor import colored, cprint
from time import sleep

con = lite.connect('D:\PROJECTES_2\python_excel\data.s3db')

with con:    
    
    cur = con.cursor()
    cur.execute('SELECT COUNT(*) FROM pelis')
    rows = cur.fetchone()
    print('Total : ' + str(rows[0]) + '\n\n')

    cur = con.cursor()    
    sql = "SELECT * FROM films WHERE title LIKE '%" + sys.argv[1]+ "%' OR "
    sql += "title LIKE '%" + sys.argv[1]+ "%' OR "  
    sql += "year LIKE '%" + sys.argv[1]+ "%' OR " 
    sql += "actors LIKE '%" + sys.argv[1]+ "%' OR " 
    sql += "director LIKE '%" + sys.argv[1]+ "%' OR " 
    sql += "type LIKE '%" + sys.argv[1]+ "%' OR " 
    sql += "sinopsis LIKE '%" + sys.argv[1]+ "%' "  
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        aux = uprint(row).replace(sys.argv[1],"***")
        v = aux.split('***')
        s = ''
        for x in range(len(v)):
            s = s+ v[x]
            if x < len(v)-1:
                s += (eval("colored('"+sys.argv[1]+"','red', attrs=['bold'])"))
        print(s)
        print("")