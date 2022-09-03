#Obtencion de raices de ec segundo grado
from math import sqrt

def discriminante(a1, b1, c1):
    d= sqrt(b1*b1-4*a1*c1)
    return d

def lectura( ):
    a= float(input("Dame el coeficiente de x^2:"))
    b= float(input("Dame el coeficiente de x:"))
    c= float(input("Dame el coeficiente independiente:"))
    return [a,b,c]

def calcular(a,b,c,d1):
    x1= (-b+d1)/2*a
    x2= (-b-d1)/2*a
    return (x1, x2)

[a,b,c]= lectura( )

d1= discriminante(a,b,c)

(x1,x2)= calcular(a,b,c,d1)
print("El resultado de x1 ",x1)
print("El resultado de x2 ",x2)