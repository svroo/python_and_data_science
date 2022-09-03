#Detector de fechas

import re
cadena="MELM8305281H0 SECM011128HDFRVRA1"

rfc= re.findall(r'[A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][0-9][0-9A-Z][0-9A-Z][0-9A-Z]\b',cadena)
curp= re.findall(r'[A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][0-9][H|M][A-Z][A-Z][A-Z][A-Z][A-Z][0-9A-Z][0-9]\b',cadena)
print(rfc)
print(curp)
print("Se encontraron", len(rfc),"rfc")
print("Se encontraron", len(curp),"curp")