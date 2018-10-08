#!/usr/bin/python3
# -*- coding: utf-8 -*-

v = [ ["08:00", "Ass1*#cccccc", "",             "Ass2*#cccccc", "",             "" ],
["09:00",       "Ass1*#cccccc", "",             "Ass2*#cccccc", "Ass2*#00cccc", "" ],
["10:00",       "Ass2*#00cccc", "Ass3*#ff0000", "Ass2*#cccccc", "",             "" ],
["11:00",       "Ass3*#00cccc", "Ass3*#ff0000", "Ass4*#cccccc", "Ass7*#00cccc",             "" ] ]

v_hores = []

v_text = []
v_color = []
v_durada = []

#HORES
def hores():
    for vv in v:
        v_hores.append(vv[0])  

hores()

for h in v_hores:
    print(h)

def valors_dia(dia):   
    
    aux =  v[0][dia]
    #print("*"+aux+"*")
    if "*" in aux:    
        text, color = aux.split("*")         
    else:
        text = ""
        color = "#ffffff"
    text_anterior = aux
    v_text.append(text)
    v_color.append(color)
    v_durada.append(1)
    i = 1
    k  = 0
    while (i < len(v)):
        aux = v[i][dia]
        if "*" in aux:
            text, color = aux.split("*")      
            if text_anterior != aux:       #nova assig
                v_text.append(text)
                v_color.append(color)
                v_durada.append(1)
                k = k + 1
            else:
                v_durada[k] = v_durada[k] + 1
        else:
            if text_anterior != aux:
                v_text.append("")
                v_color.append(color)
                v_durada.append(1)
                k = k + 1
            else:
                v_durada[k] = v_durada[k] + 1

        text_anterior=aux
        i = i + 1

for dia in range(1, 6):
    print("*****DIA = "+str(dia)+"*******")
    valors_dia(dia)
    r = 0
    for r in range(len(v_text)):   
        print(v_text[r])
        print(v_color[r])
        print(v_durada[r])                
    v_text = []
    v_color = []
    v_durada = []
    print("*********************")
