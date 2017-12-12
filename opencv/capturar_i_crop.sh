#!/bin/sh

sudo killall chromium
chromium --noerrdialogs --disable-session-crashed-bubble --disable-infobars --kiosk https://www.raspberrypi.org/blog/ &
scrot captura_pantalla.png -d10 #10 seconds delay | dono temps a carregar la pàgina

sleep 3
python crop_image.py &	#tancar popup per continuar programa

sleep 2
tesseract captura_pantalla_crop.png text #afegeix extensió .txt

cat text.txt
