import sys
import platform

PAGINA_ACTUAL = ""
POP_UP_NUM_ON = False

if platform.system() == "Windows":
    RUTA_BBDD = "C:\\Users\\externo101\\Documents\\PROVES_SERGI\\Python_SQLite\\dades.s3db"
else:
    RUTA_BBDD = "/home/pi/Desktop/dades.s3db"
