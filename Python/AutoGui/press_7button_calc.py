import time
import pyautogui

time.sleep(2)
button7location = pyautogui.locateOnScreen('calc7key.png')
print(button7location)
button7x, button7y = pyautogui.center(button7location)
pyautogui.click(button7x, button7y)  # clicks the center of where the 7 button was found