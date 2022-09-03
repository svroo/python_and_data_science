import csv

with open('profes.csv','w',encoding='utf-8', newline='') as arch:
    campos=['Materia','Profesor']
    escritor= csv.DictWriter(arch, fieldnames=campos)

    escritor.writeheader()
    escritor.writerow({'Materia': 'Matematicas', 'Profesor': 'Juan Perez'})
    escritor.writerow({'Materia': 'Física', 'Profesor': 'Alberto una Piedra'})
    escritor.writerow({'Materia': 'Química', 'Profesor': 'Maria Curie'})
    escritor.writerow({'Materia': 'Historia', 'Profesor': 'Benito Hidalgo'})

