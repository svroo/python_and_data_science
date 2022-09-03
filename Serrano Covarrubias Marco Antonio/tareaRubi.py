import numpy as np

#Asignacion de columnas y filas
m= int(input("Ingrese la cantidad de columnas: \n"))
n= int(input("Ingrese la cantidad de filas: \n"))

#Creacion de matriz
matA=np.arange(n*m).reshape(n,m)
print("La matriz de",m,"x",n,"ha sido creada\n")

for i in range(n):
    for j in range(m):
        matA[i][j]=input("Ingrese numero: ")

print("La matriz es la siguiente:\n")
print(matA)

#Impresion de izquierda a derecha de arriba hacia abajo
print("\nImpresion de arriba hacia abajo y de izquierda a derecha")

for i in range(n):
    for j in range(m):
        print(matA[i][j])

print("\nImpresion de abajo hacia arriba y de izquierda a derecha")

for i in range(n-1,-1,-1):
    for j in range(m):
        print(matA[i][j])

print("\nImpresion de arriba hacia abajo,\n y en filas impares de derecha a izquierda\n y filas pares de izquierda a derecha")

for i in range(n):
    if i%2==0:
        for j in range(m):
            print(matA[i][j])
    else:
        for j in range(m-1,-1,-1):
            print(matA[i][j])

print("\nLa diagonal desde la parte inferior izquierda hacia arriba")

if i==m:
    for i in range(n):
        print(matA[i][i])
else:
    print("Error, la matriz no es cuadrada")
