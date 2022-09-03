#Obtencion de raices de ec segundo grado
def lectura( ):
    a1= int(input("Dame la parte natural del 1er numero complejo: "))
    a2= int(input("Dame la parte compleja del 1er numero complejo: "))
    b1= int(input("Dame la parte natural del 2do numero complejo:  "))
    b2= int(input("Dame la parte compleja del 1er numero complejo: "))
    return [a1,a2,b1,b2]

def suma(a1,a2,b1,b2):
    sum1= a1+b1
    sum2= a2+b2
    print("El resultado de la suma es: ",sum1, "+",sum2,"j")

def resta(a1,a2,b1,b2):
    res1= a1-b1
    res2= a2-b2
    print("El resultado de la suma es: ",res1, "+",res2,"j")
    
def mult(a1,a2,b1,b2):
    mul1=a1*b1
    mul2=a2*b2
    print("El resultado de la suma es: ",mul1, "+",mul2,"j")
    
def divi(a1,a2,b1,b2):
    div1= a1/b1
    div2= a2/b2
    print("El resultado de la suma es: ",div1, "+",div2,"j")

numeros= lectura()
opc=input("Ingrese la operacion a realizar:")
if opc=="1":
    suma(numeros[0], numeros[1], numeros[2], numeros[3])
elif opc=="2": 
    resta(numeros[0], numeros[1], numeros[2], numeros[3])
elif opc=="3":

    mult(numeros[0], numeros[1], numeros[2], numeros[3])
elif opc=="4":

    divi(numeros[0], numeros[1], numeros[2], numeros[3])
else:
    print("Opción no válida")


    

 
