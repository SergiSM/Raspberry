import time
import pyautogui

time.sleep(3)

pyautogui.click(x=100, y=200)

'''pyautogui.moveTo(100, 150)
pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
pyautogui.dragTo(100, 150)
pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down'''


'''x = 100
for i in range(5):
    pyautogui.moveTo(x, 300)
    x = x + 300
    time.sleep(1)'''


'''screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')'''


#This example drags the mouse in a square spiral shape in MS Paint (or any graphics drawing program):
'''distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.5)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.5)  # move up'''

#https://pyautogui.readthedocs.io/en/latest/cheatsheet.html

#pyautogui.typewrite('Hello world!\n', interval=0.5)  # useful for entering text, newline is Enter

'''pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
pyautogui.prompt('This lets the user type in a string and press OK.')'''

#pyautogui.screenshot()  # returns a Pillow/PIL Image object
#pyautogui.screenshot('foo.png')  # returns a Pillow/PIL Image object, and saves it to a file

#If you have an image file of something you want to click on, you can find it on the screen with locateOnScreen()
#pyautogui.locateOnScreen('looksLikeThis.png') # returns (left, top, width, height) of first place it is found(863, 417, 70, 13)

#pixel matching
im = pyautogui.screenshot()
im.getpixel((100, 200))

pyautogui.pixel(100, 200)
pyautogui.pixelMatchesColor(100, 200, (130, 135, 144)) #, tolerance=10

im = pyautogui.screenshot(region=(0,0, 300, 400))
