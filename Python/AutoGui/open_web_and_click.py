# -*- coding: utf-8 -*-
import time
import pyautogui
import webbrowser, os, sys

url = "https://www.google.com"

chrome_path = '/usr/lib/chromium-browser/chromium-browser'
webbrowser.get(chrome_path).open(url)

time.sleep(3)

#pyautogui.click(x=90, y=120)  #click about us link

pyautogui.click(x=180, y=300)   #barra de cerca
pyautogui.write('ESP32', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('enter')  # press the Enter key

time.sleep(10) #espero que es carregui la pàgina

pyautogui.click(x=180, y=300) #click sobre el primer link

time.sleep(10) #espero que es carregui la pàgina

#guardar pàgina web
pyautogui.click(button='right')  # right-click the mouse
pyautogui.hotkey('ctrl', 's')
time.sleep(3)
pyautogui.press('enter') 
