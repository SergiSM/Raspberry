#!/usr/bin/python3
# -*- coding: utf-8 -*-

v = [ ["08:00", "Ass1*#cccccc", "", "Ass2*#cccccc", "", "Ass1*#cccccc" ],
["09:00", "Ass1*#cccccc", "", "Ass2*#cccccc", "", "Ass1*#cccccc" ],
["10:00", "Ass2*#00cccc", "Ass3*#ff0000", "Ass2*#cccccc", "", "Ass1*#cccccc" ] ]

v_hores = []

v_text = []
v_color = []
v_durada = []

def hores():
    for vv in v:
        v_hores.append(vv[0])

hores()

for h in v_hores:
    print(h)

def valors_dia(dia):   
    aux =  v[0][dia]
    #print(aux)
    if "*" in aux:    
        text, color = aux.split("*")     
        text_anterior = text
    else:
        text = ""
        color = "#ffffff"
        text_anterior = ""
    v_text.append(text)
    v_color.append(color)
    v_durada.append(1)
    i = 1
    k  = 0
    while (i < len(v)):
        aux = v[i][dia]
        if "*" in aux:
            text, color = aux.split("*")      
            if text_anterior != text:       #nova assig
                v_text.append(text)
                v_color.append(color)
                v_durada.append(1)
                k = k + 1
            else:
                v_durada[k] = v_durada[k] + 1
        else:
            v_durada[k] = v_durada[k] + 1
        i = i + 1

dia = 1
for dia in range(7):
    valors_dia(dia)
    r = 0
    for r in range(len(v)-1):
        print(v_text[r])
        print(v_color[r])
        print(v_durada[r])
    v_text = []
    v_color = []
    v_durada = []
    print("*********************")
