# -*- coding: utf-8 -*-
# pylint: disable=C0103
from bs4 import BeautifulSoup
import requests
import urllib.request
import subprocess

def Bricogeek(url):    
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:

        html = BeautifulSoup(req.text, "html.parser")

        score = html.find_all('h2', {'itemprop' : 'headline'})
        for s in score:
            t = s.getText()
            a = s.find('a')
            print(t + " --- " +a.attrs['href'])
    else:
        print("Status Code %d" %statusCode)

def Soloelectronicos(url):
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:

        html = BeautifulSoup(req.text, "html.parser")

        score = html.find_all('a', {'rel' : 'bookmark'})
        for s in score:
            print(s.getText()+"  ---  "+s.attrs['href'])
    else:
        print("Status Code %d" %statusCode)

def Raspberry(url):
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:

        html = BeautifulSoup(req.text, "html.parser")
        score = html.find_all('h1')
        for s in score:
            t = s.getText()
            print(t)
            if s.find('a'):
                a = s.find('a')
                t = t + " --- " +a.attrs['href']
    else:
        print("Status Code %d" %statusCode)

def Adafruit(url):
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:

        html = BeautifulSoup(req.text, "html.parser")

        tags = ['links new', 'links featured']
        for TAG in tags:
            for score in html.find_all('ul', {'class': TAG}):
                for s in score.find_all('li'):
                    score = s.find('a', {'class': 'name'})
                    print(score.getText().strip()+"  ---  "+score.attrs['href'])

    else:
        print("Status Code %d" %statusCode)


def Save_img(url):
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:

        html = BeautifulSoup(req.text, "html.parser")        
        score = html.find_all('img', {'itemprop' : 'url'})
        i = 0
        for s in score:                
            try:                   
                if (s.attrs['alt'] != "logo"): 
                    print(s.attrs['src'])                          
                    imatge = s.attrs['src']                        
                    #urllib.request.urlretrieve(imatge, "c:\\Temp\\"+str(i)+imatge[-4:])        
                    urllib.request.urlretrieve(imatge, str(i)+imatge[-4:])        
                    i = i + 1
            except:
                pass
    else:
        print("Status Code %d" %statusCode)

'''Bricogeek("http://blog.bricogeek.com")
Soloelectronicos("http://soloelectronicos.com/")
Raspberry("https://www.raspberrypi.org/blog/")
Adafruit("https://blog.adafruit.com")'''

#Save_img("http://blog.bricogeek.com")

#subprocess.run(['git add .'])
'''subprocess.run(['git add 0.jpg'])
subprocess.run(['git commit -m "prova"'])
subprocess.run(['git push origin master'])'''
#subprocess.run(['notepad.exe', 'C:\\Temp\\new.txt'])
