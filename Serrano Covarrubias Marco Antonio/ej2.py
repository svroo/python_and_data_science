m= int(input("Dame el No. de renglones"))
n= int(input("Dame el No. de columnas"))
A= [ ]

for i in range(m):
    A.append([ ])
    for j in range (n):
        A[i].append([None])

for i in range(m):
    print()
    for j in range(n):
        print(A[i][j],"it", end =",")

