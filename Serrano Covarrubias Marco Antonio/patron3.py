import re
cadena="Hoy tengo 5 clases de python desde las 7:45 hasta las 15:37. Hoy es un viernes"

print(re.findall(r'\d',cadena))

print(re.findall(r'\b[0-9]+',cadena))

print(re.findall(r'[0-9]+',cadena))

print(re.findall(r'[0-9]+:[0-9]+',cadena))

print(re.findall(r'[0-9]+\.[0-9]?',cadena))