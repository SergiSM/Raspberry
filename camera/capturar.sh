#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

sudo raspistill -o /var/www/html/$DATE.jpg -p 0,0,800,480 -w 640 -h 480 -q

#tesseract imatge.jpg resultat
