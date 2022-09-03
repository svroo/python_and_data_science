import csv, operator

archCSV =open('profes.csv')
lector = csv.DictReader(archCSV)
listDicc= list(lector)
listDiccOrd= sorted(listDicc,
                    key=operator.itemgetter('Profesor'),
                    reverse=False)
for registro in listDiccOrd:
    print(registro)