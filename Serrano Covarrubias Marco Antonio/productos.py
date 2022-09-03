
x=1
total=0
codigo= dict()

codigo= {
    "Taco": 15, "Agua":10,
    "Galleta":8, "Chocolate":12,
    "Refresco": 15
}

print("Menu:")
for k,v in codigo.items():
    print("%s -> %i"%(k,v))
while(x!=0):
    j=input("Ingrese el objeto que va a comprar: ")
    valores= codigo.get(j)
    n=int(input("Cuantos desea comprar: "))
    total= total+(valores*n)
    x=int(input("Desea seguir comprando?\n 1 -> Si\n 0 -> No\n"))
print("El costo total va a ser de:",total)