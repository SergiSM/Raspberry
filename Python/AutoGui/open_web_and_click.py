import time
import pyautogui
import webbrowser, os, sys

url = "https://www.google.com"

chrome_path = '/usr/lib/chromium-browser/chromium-browser'
webbrowser.get(chrome_path).open(url)

time.sleep(3)

pyautogui.click(x=90, y=120) #about us link
