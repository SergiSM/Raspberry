# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import sqlite3 as lite

con = lite.connect('D:\\PROJECTES_2\\Raspberry\\basket.s3db')

url = "http://www.euroleague.net/main/results/showgame?gamecode="+sys.argv[1]+"&seasoncode=E2016"
req = requests.get(url)
statusCode = req.status_code
if statusCode == 200:

    html = BeautifulSoup(req.text, "html.parser")
    #print(html.title.string)
    id_web = sys.argv[1]
    local = html.find('span', {'id': 'ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_LocalClubStats_lblTeamName'}).getText()
    visitor = html.find('span', {'id': 'ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_RoadClubStats_lblTeamName'}).getText()
    print(local)
    print(visitor)
    #score = html.find('span', {'class' : lambda L: L and L.startswith('score homepts')}).getText()
    score = html.find_all('span', {'class' : 'score'})
    local_points = score[0].getText()
    visitor_points = score[1].getText()
    print(local_points)
    print(visitor_points)

    with con:
        cur = con.cursor()
        cur.execute("SELECT id FROM games WHERE local = ? AND visitor = ?", (local,visitor,))
        data=cur.fetchone()
        if data is None:
            cur.execute("INSERT INTO games (local,visitor,local_points,visitor_points) VALUES ('"+local+"','"+visitor+"',"+str(local_points)+","+str(visitor_points)+")")
            id_game = cur.lastrowid
        else:
            id_game = data[0]

    id_base = 'ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_'
    ids = ['LocalClubStats','RoadClubStats']
    team_name = [local, visitor]
    for team in range(2):
        for x in range(1,13):
            player2 = html.find('a',{'id': id_base + ids[team] + '_repTeamStats_ctl'+format(x, '02d')+'_lnkPlayerName'})
            print(player2.contents[0])
            player = player2.contents[0]

            with con:
                cur = con.cursor()
                cur.execute("SELECT id FROM players WHERE name = ?", (player,))
                data=cur.fetchone()
                if data is None:
                    sql = "INSERT INTO players (name,team) VALUES ('"+player+"','"+team_name[team]+"')"
                    print(sql)
                    cur.execute(sql)
                    id_player = cur.lastrowid
                else:
                    id_player = data[0]

            table = html.find(id=id_base + ids[team] + "_repTeamStats_ctl"+format(x, '02d')+"_lnkPlayerName")
            
            nextNode = table.findNext('td')
            trama = nextNode.contents[0]
            if (nextNode.contents[0] == 'DNP'):
                fields = ['0']
            else:
                fields = [nextNode.contents[0]]
            for i in range(15):
                nextNode = nextNode.findNext('td')
                aux = nextNode.contents[0]
                if (aux.strip() == '' or aux == '-' or aux == 'DNP'): #strip remove blank spaces
                    aux = "0"
                trama += "," + aux
                fields.append(aux)

            #for elem in fields:
            #    print(elem)
            
            print(trama)
            with con:
                cur = con.cursor()
                sql = "INSERT INTO statistics (id_web,id_game,id_player,player,min,points,fg2,fg3,ft,r_o,r_f,assists,steals,turnovers,blocks_fv,blocks_ag,fouls_cm,fouls_rv,val) VALUES ("+str(id_web)+","+str(id_game)+","+str(id_player)+",'"+player+"','"+fields[0]+"',"+fields[1]+",'"+fields[2]+"','"+fields[3]+"','"+fields[4]+"',"+fields[5]+","+fields[6]+","+fields[8]+","+fields[9]+","+fields[10]+","+fields[11]+","+fields[12]+","+fields[13]+","+fields[14]+","+fields[15]+")"
                print(sql)
                cur.execute(sql) 

else:
    print("Status Code %d" %statusCode)