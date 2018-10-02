#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

master = Tk()
master.geometry("800x480+0+0")
master.attributes("-fullscreen", True) 

#valors obtinguts dels horaris en html
l_colors = [['silver', 'blue', 'green'], ['red','orange','yellow', 'green']]
l_text = [['Assig1', 'Assig2', 'Assig3'], ['Assig10', 'Assig22', 'Assig33', 'Asig44']]
l_hores = [[1,2,3], [2,1,2,3]]

controls = []

def clicked(event):
	#borro controls anteriors
	for c in controls:
		w.delete(c)    #delete(ALL)            

	cota = 480 / 5  # 480 ample, 5 dies
	print(str(cota))
	if event.y >= 0 and event.y <= cota:
		txt = "Divendres"            
		carregar_dia(0)
	if event.y >= cota and event.y <= cota*2:
		txt = "Dijous"
		carregar_dia(1)

	w.itemconfig(titol, text=txt)            
	print('Got object click', event.x, event.y)
	print(event.widget.find_closest(event.x, event.y))                        
	

def carregar_dia(dia):            
	#colors = ['silver', 'blue', 'green']
	#text = ['Assig1', 'Assig2', 'Assig3']
	#hores = [1, 2, 3]
	colors = l_colors[dia]
	text = l_text[dia]
	hores = l_hores[dia]
	i = 0
	ample = 50
	left = 50
	for h in hores:
		r = w.create_rectangle(left, 0, left+ h*ample, 380, fill=colors[i], outline = 'black')
		controls.append(r)
		t = w.create_text(left + 20, 200, anchor = 'nw', text=text[i], fill='black', font=('Arial', '10','bold'), angle=90)
		controls.append(t)
		left = left + h*ample
		print(left)
		i = i + 1

w = Canvas(master, width=800, height=480, bg="black")
w.pack()


w.create_rectangle(0, 0, 50, 480, fill='blue', outline = 'black')
titol = w.create_text(20, 200, text="Divendres", fill='white', font=('Arial', '12','bold'), angle=90)

top = 0   
ample = 50
llarg = 100
left = 50   
hh = ["08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "17:00 - 18:00", "18:00 - 19:00", "19:00 - 20:00"]        
for i in range(12): 
	w.create_rectangle(left, 380, left + ample, 480, fill='silver', outline = 'black')  #outline=border            
	w.create_text(left+20, 430, anchor = 'center', text=hh[i], fill='black', font=('Arial', '10','bold'), angle=90)                        
	left = left + ample
	
top = 0
ample = 480/5

w.create_rectangle(720, top, 800, top + int(ample), fill='blue', outline = 'white', tags="playbutton")
w.tag_bind("playbutton","<Button-1>", clicked)
w.create_text(760, top + 45, text="Divendres", fill='white', font=('Arial', '12','bold'), angle=90, tags="playbutton")
top = top + ample

w.create_rectangle(720, top, 800, top + int(ample), fill='blue', outline = 'black', tags="playbutton")
w.tag_bind("playbutton","<Button-1>", clicked)
w.create_text(760, top + 50, text="Dijous", fill='white', font=('Arial', '12','bold'), angle=90, tags="playbutton")
top = top + ample

master.mainloop()
