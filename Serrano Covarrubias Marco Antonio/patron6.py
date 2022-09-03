import re
cadena="SECM011128HDFRVRA1"
curp= re.findall(r'[A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][0-9][H|M][A-Z][A-Z][A-Z][A-Z][A-Z][0-9A-Z][0-9]\b',cadena)

print(curp)

print("Se encontraron", len(curp),"curp")