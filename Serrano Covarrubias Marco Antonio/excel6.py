import csv, operator
archCVS= csv.reader(open('profes.csv'))
listaOrd = sorted(archCVS,key=operator.itemgetter(1),reverse=True)
print(listaOrd)