import csv

with open('./profes.csv') as archCVS:
    lectorCSV= csv.reader(archCVS, delimiter=',')
    contLinea = 0
    for linea in lectorCSV:
        if contLinea==0:
            print(f'El encabezado es {",".join(linea)}')
            contLinea +=1
        else:
            print(f'El profesor\t{linea[1]} imparte la materia {linea[0]}.')
            contLinea +=1
    print(f'Se imprimeron {contLinea} lineas.')
