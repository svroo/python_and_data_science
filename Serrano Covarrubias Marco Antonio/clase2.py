import csv

miLista = [["num", "materia", "profesor"],
           [1, "Matemáticas", "Juan Perez"],
           [2, "Física", "Alberto una Piedra"],
           [3, "Química", "Maria Curie"],
           [4, "Historia", "Benito Hidalgo"]]

with open('profes.csv','w', newline='') as arch:
    escritor= csv.writer(arch)
    escritor.writerows(miLista)