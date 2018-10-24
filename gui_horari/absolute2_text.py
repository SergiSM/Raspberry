def carregar_dia(dia):            
    #colors = ['silver', 'blue', 'green']
    #text = ['Assig1', 'Assig2', 'Assig3']
    #hores = [1, 2, 3]
    colors = self.colors[dia]
    text = self.text[dia]
    hores = self.hores[dia]
    i = 0
    ample = 50
    left = 50
    for h in hores:
        r = self.w.create_rectangle(left, 0, left+ h*ample, 380, fill=colors[i], outline = 'black')
        self.controls.append(r)                
        t = self.w.create_text(left + 20, 200 + 2.5*len(text[i]), anchor = 'nw', text=text[i], fill='black', font=('Arial', '10','bold'), angle=90)
        self.controls.append(t)
        left = left + h*ample
        i = i + 1    
