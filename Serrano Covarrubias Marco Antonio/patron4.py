#Detector de fechas

import re
cadena="Hoy tengo 5 clases de python desde las 7:45 hasta las 15:37. Hoy es un viernes 20.11.20213 b 12-12-2012 c 13/01/2015"

date= re.findall(r'[0-9][0-9][.|/|-][0-9][0-9][.|/|-][0-9][0-9][0-9][0-9]\b',cadena)

print(date)

print("Se encontraron", len(date),"fechas")
