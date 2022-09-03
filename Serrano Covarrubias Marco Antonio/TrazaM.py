
suma=0
i=0
j=0

A=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(A)):
    suma= suma+A[i][i]  
print(suma)

print("La transpuesta es:")

for i in range(len(A)):
    print( )
    for j in range(len(A)):
        print(A[j][i], end=" ")