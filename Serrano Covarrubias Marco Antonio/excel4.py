import csv
with open('profes.csv', newline='', encoding='utf-8') as archCVS:
    lector= csv.reader(archCVS, delimiter=' ')
    for linea in lector:
        print(', '.join(linea))
        
        