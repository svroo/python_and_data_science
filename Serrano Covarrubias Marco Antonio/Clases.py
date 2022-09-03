import re
cadena="Hoy hay clases de python. Hoy por Hoy es Jueves"

print(re.search("python", cadena))

patron= "Hoy"

if(re.search(patron, cadena))is not None:
    print("Se encontro patron")
else:
    print("No se encontro")
    
res =re.search(patron, cadena)
print(res)
