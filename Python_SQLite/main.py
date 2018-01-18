#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import sqlite3 as lite  

con = lite.connect("C:\\Users\\externo101\\Documents\\PROVES_SERGI\\Python_SQLite\\dades.s3db")


with con:
    
    cur = con.cursor() 

    #cur.execute("SELECT COUNT(*) FROM players WHERE name = ?", (name,))
    cur.execute("SELECT COUNT(*) FROM players")
    data=cur.fetchone()     #tuple
    print("TOTAL = " + str(data[0]))          #first field
    #if data==0:
    #    cur.execute("INSERT INTO aux (title) VALUES ('"+title+"')")

    if len(sys.argv) == 1:
        cur.execute("SELECT name, team FROM players ORDER BY name")        
    else:
        cur.execute("SELECT name, team FROM players WHERE team LIKE '%"+sys.argv[1]+"%'")
        #cur.execute("SELECT name, team FROM players WHERE team LIKE ?", (sys.argv[1],))
    rows = cur.fetchall()
    #for row in rows:
    #    print(row)  #tuple

    sql = []
    '''sql.append("SELECT * FROM games WHERE local LIKE '%"+sys.argv[1]+"%' OR visitor LIKE '%"+sys.argv[1]+"%'")    
    

    sql.append("SELECT player, points FROM statistics WHERE id_game IN (SELECT id FROM games WHERE local LIKE '%"+sys.argv[1]+"%' AND local_points > visitor_points UNION SELECT id FROM games WHERE visitor LIKE '%"+sys.argv[1]+"%' AND local_points < visitor_points)")    
    sql.append("SELECT SUM(points),player FROM statistics GROUP BY player ORDER BY SUM(points) DESC")
    sql.append("SELECT AVG(points),player FROM statistics GROUP BY player ORDER BY AVG(points) DESC")'''
    sql.append("SELECT DISTINCT(local) FROM games ORDER BY local")
    sql.append("SELECT COUNT(*),local FROM games GROUP BY local HAVING local_points > visitor_points")
    sql.append("SELECT * FROM games WHERE local LIKE '%"+sys.argv[1]+"%' AND local_points > visitor_points UNION SELECT * FROM games WHERE visitor LIKE '%"+sys.argv[1]+"%' AND local_points < visitor_points")
    sql.append("SELECT * FROM games WHERE local LIKE '%"+sys.argv[1]+"%' OR visitor LIKE '%"+sys.argv[1]+"%'")
    sql.append("SELECT (SELECT COUNT(*) FROM games WHERE local LIKE '%"+sys.argv[1]+"%' AND local_points > visitor_points) + (SELECT COUNT(*) FROM games WHERE visitor LIKE '%"+sys.argv[1]+"%' AND local_points < visitor_points) AS victorias") 
    sql.append("SELECT (SELECT COUNT(*) FROM games WHERE local LIKE '%"+sys.argv[1]+"%' OR visitor LIKE '%"+sys.argv[1]+"%') - ((SELECT COUNT(*) FROM games WHERE local LIKE '%"+sys.argv[1]+"%' AND local_points > visitor_points) + (SELECT COUNT(*) FROM games WHERE visitor LIKE '%"+sys.argv[1]+"%' AND local_points < visitor_points)) AS derrotas") 
    sql.append("SELECT (SELECT COUNT(*) FROM games WHERE local LIKE '%"+sys.argv[1]+"%' AND local_points > visitor_points) + (SELECT COUNT(*) FROM games WHERE visitor LIKE '%"+sys.argv[1]+"%' AND local_points < visitor_points) AS victorias") 
    sql.append("SELECT points,local,visitor FROM statistics s, games g WHERE s.id_game=g.id AND player LIKE '%"+sys.argv[1]+"%'")

    for sql_ in sql:
        cur.execute(sql_)
        rows = cur.fetchall()
        for row in rows:
            print(row)  #tuple
        print("**********")
