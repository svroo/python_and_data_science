
import matplotlib.pyplot as plt
import csv
path='E:/Python/'
with open(path+'horario.csv','r') as csvfile:
    readCSV= csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if(row[0]+row[1]+row[2]=='28079004' and row[3]=='12'):
            plt.title("Oxido de nitrogeno:"+ row[8]+ "/"+row[7]+"/"+ row[6])
            hora = 0
            
            vmch = 9
            valValido=[]
            horas=[]
            while hora <= 23:
                if row[vmch+2*hora+1] == 'V':
                    valValido.append(row[vmch+2*hora])
                    horas.append(hora)
                hora= hora+1
            plt.plot(horas,valValido)
            plt.show()

