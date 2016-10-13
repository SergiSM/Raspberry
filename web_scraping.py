# -*- coding: utf-8 -*-
__author__ = 'Swan'

from bs4 import BeautifulSoup
import requests

url = "http://www.euroleague.net/main/results/showgame?gamecode=4&seasoncode=E2016"

# Realizamos la petición a la web
req = requests.get(url)

# Comprobamos que la petición nos devuelve un Status Code = 200
statusCode = req.status_code
if statusCode == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    #print(html.find_all(["a", "b"]))
    #print(html.find_all(id="ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_LocalClubStats_repTeamStats_ctl01_lnkPlayerName"))

    #address = soup.find(text="Address:")
    '''print(table.findNext('td').contents[0])
    print(table.findNext('td').findNext('td').contents[0])
    print(table.findNext('td').findNext('td').findNext('td').contents[0])'''
    for x in range(1,13):
        player = html.find('a',{'id':'ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_LocalClubStats_repTeamStats_ctl'+format(x, '02d')+'_lnkPlayerName'})
        print(player.contents[0])
        table = html.find(id="ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_LocalClubStats_repTeamStats_ctl"+format(x, '02d')+"_lnkPlayerName")
        
        nextNode = table.findNext('td')
        trama = nextNode.contents[0]
        for i in range(15):
            nextNode = nextNode.findNext('td')
            aux = nextNode.contents[0]
            #aux = nextNode.findNext('td').contents[0]
            #print('*'+aux+'*')
            #if (aux == ):
            #    aux = "0"
            trama += "," + aux
        
        print(trama)

    link_vis = 'ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_RoadClubStats_repTeamStats_ctl'
    for x in range(1,13):
        player = html.find('a',{'id':link_vis+format(x, '02d')+'_lnkPlayerName'})
        print(player.contents[0])
        table = html.find(id=link_vis+format(x, '02d')+"_lnkPlayerName")
        
        nextNode = table.findNext('td')
        trama = nextNode.contents[0]
        for i in range(15):
            nextNode = nextNode.findNext('td')
            aux = nextNode.contents[0]
            #print('*'+aux+'*')
            #if (aux == ):
            #    aux = "0"
            trama += "," + aux
        
        print(trama)

    #print(html.find(id="ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_LocalClubStats_repTeamStats_ctl01_lnkPlayerName").findNext('td').findNext('td').contents[0])

    # Obtenemos todos los divs donde estan las entradas
    entradas = html.find_all('td',{'class':'PlayerContainer'})

    # Recorremos todas las entradas para extraer el título, autor y fecha
    for i,entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
        player = entrada.find('a',{'id':'ctl00_ctl00_ctl00_ctl00_maincontainer_maincontent_contentpane_boxscorepane_ctl00_LocalClubStats_repTeamStats_ctl01_lnkPlayerName'})
        '''titulo = entrada.find('span', {'class' : 'tituloPost'}).getText()
        # Sino llamamos al método "getText()" nos devuelve también el HTML
        autor = entrada.find('span', {'class' : 'autor'})

        # Imprimo el Título, Autor y Fecha de las entradas
        print "%d - %s  |  %s  |  %s" %(i+1,titulo,autor,fecha)'''
        #print(player)

else:
    print("Status Code %d" %statusCode)
