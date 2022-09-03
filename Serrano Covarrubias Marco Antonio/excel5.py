import csv

with open('profes.csv', mode='r') as archCVS:
    lector = csv.DictReader(archCVS)
    contLinea = 0
    for linea in lector:
        if contLinea==0:
            print(f'El encabezado es {",".join(linea)}')
            contLinea +=1
        print(f'El profesor\t{linea["Profesor"]} imparte la materia {linea["Materia"]}.')
        contLinea +=1
    print(f'Se imprimeron {contLinea} lineas.')