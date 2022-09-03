m= int(input("Dame el No. de renglones"))
n= int(input("Dame el No. de columnas"))
A= [ ]

A= [[j**2 for i in range(n)] for j in range(m)]
print(A)

for i in range(m):
    print()
    for j in range (n):
        print(j,"it", end =",")        