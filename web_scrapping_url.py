# -*- coding: utf-8 -*-
# pylint: disable=C0103
from bs4 import BeautifulSoup
import requests

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

Bricogeek("http://blog.bricogeek.com")
Soloelectronicos("http://soloelectronicos.com/")
Raspberry("https://www.raspberrypi.org/blog/")
