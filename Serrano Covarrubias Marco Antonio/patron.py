import re

cadena="Hoy tengo 5 clases de python desde las 7.0 hasta las 15. Hoy es un viernes del 2021"

print(re.findall(r'\d',cadena))

print(re.findall(r'[0-9]+',cadena))

print(re.findall(r'[0-9]+l.[0-9]', cadena))