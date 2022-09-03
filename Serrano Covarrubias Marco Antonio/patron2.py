from itertools import count
import re

cadena="Hoy tengo 0XA5 clases 0xA5 de python 0x.BA desde las 0XB3 0X33 7.0 hasta las 15. 0xa3 Hoy es un viernes del 2021"

#Decimal
Dec= re.findall(r'[0-9]+',cadena)
print(Dec)

#Hexadecimal
Hex= re.findall(r'[0]+[Xx]+[0-9A-Fa-f]+',cadena)
print(Hex)

print("Hay",len(Dec), "numeros decimales")
print("Hay",len(Hex), "numeros hexadecimales")