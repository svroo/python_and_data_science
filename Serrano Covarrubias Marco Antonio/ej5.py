A=[[9,12,1,44],[16,7,2,14],[2,3,1,8],[2,-5,-6,0]]
b=[ ]
j=int(input("Ingrese la columna que desea accesar: "))

for i in range(len(A)):
    b.append(A[i][j])

print(b)