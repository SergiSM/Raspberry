#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import datetime

'''inici = datetime.datetime.strptime("2019-04-12 10:15:56", '%Y-%m-%d %H:%M:%S')
print(type(inici))
fi = datetime.datetime.now()
print(type(fi))
diferencia = fi - inici
print(diferencia)'''

def codi_fase(codi):
    if (codi[0:2] == "00"):
        try:
            aux = str(p[producte]).split(';')
            hora_inici = aux[0][:-7]
            hora_fi = datetime.datetime.now()            
            f = open(datetime.datetime.now().strftime("%Y_%m_%d")+".csv", "a")
            f.write(producte + ";P"+aux[1]+";" + str(hora_inici) + ";" + str(hora_fi.strftime('%d-%m-%Y %H:%M:%S')) + ";" + codi + ";ERROR" + "\n")
            f.close()
            del p[producte] #l'elimino del diccionari
        except:
                print("No hi ha hora inici")
    else:        
        if codi[-1:] == "1":    #últim dígit -> 1 = inici fase, 2=fi fase
            p[producte] = str(datetime.datetime.now())+";"+codi[-2:-1]
        else:
            try:
                #hora_inici = p[producte]
                aux = str(p[producte]).split(';')
                hora_inici = datetime.datetime.strptime(aux[0], '%Y-%m-%d %H:%M:%S')
                hora_fi = datetime.datetime.now()
                diferencia = hora_fi - hora_inici
                p[producte] = str(p[producte]) + ", " + str(hora_fi) + ", " + str(diferencia)
                f = open(datetime.datetime.now().strftime("%Y_%m_%d")+".csv", "a")
                f.write(producte + ";P"+codi[-2:-1]+";" + str(hora_inici.strftime('%d-%m-%Y %H:%M:%S')) + ";" + str(hora_fi.strftime('%d-%m-%Y %H:%M:%S')) + ";" + str(diferencia)[:-7] + "\n")
                f.close()
                for x, y in p.items():
                    print(x, y)
                del p[producte] #l'elimino del diccionari
            except:
                print("No hi ha hora inici")

p = {}
while True:    
    codi = raw_input(" ... ")        
    if (len(codi) > 9):
        producte = codi
        if producte not in p:
            p[producte] = ""
        #for x in p:
            #print(x)
        for x, y in p.items():
            print(x, y)
    else:
        codi_fase(codi)

    
