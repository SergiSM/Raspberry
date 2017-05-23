from bs4 import BeautifulSoup
from colored import fg, bg, attr
import requests

url = r"C:\Users\externo101\Documents\PROVES_SERGI\Soup\soloelectronicos.html"
f = open(url, encoding="utf8").read()
html = BeautifulSoup(f, "html.parser")
print(html.title.string)

score = html.find_all('a', {'rel' : 'bookmark'})
print(score[0].getText())
print(score[1].getText())

for s in score:
    print(s.getText()+"  ---  "+s.attrs['href'])

url = r"C:\Users\externo101\Documents\PROVES_SERGI\Soup\blogbricogeek.html"
f2 = open(url, encoding="utf8").read()
html = BeautifulSoup(f2, "html.parser")
score = html.find_all('h2', {'itemprop' : 'headline'})
for s in score:
    t = s.getText()
    a = s.find('a')
    t = t + " --- " +a.attrs['href']
    print(t)

url = r"C:\Users\externo101\Documents\PROVES_SERGI\Soup\raspberry.html"
f2 = open(url, encoding="utf8").read()
html = BeautifulSoup(f2, "html.parser")
score = html.find_all('h1')
for s in score:
    t = s.getText()
    if s.find('a'):
        a = s.find('a')
        t = t + " --- " +a.attrs['href']
    print(t)
