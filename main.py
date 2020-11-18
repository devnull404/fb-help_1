import numpy as np
import random as rn

n, m = [9, 10]

A = np.zeros((n, m), dtype=int)
B =np.zeros((n+2, m+2), dtype=int)

for i in range(n):
    for j in range(m):
        A[i,j] = rn.randint(0,1)

B[1:-1, 1:-1] = A

for i in range(1, n+1):
    for j in range (1, m+1):
        print(B)
        arguments = B[i+1,j]+B[i-1,j]+B[i,j+1]+B[i,j-1]
        if B[i,j] == 1 and (arguments >= 3 and arguments <=4):
            B[i,j] = 0
        if B[i,j] == 0 and (arguments >= 1 and arguments <= 2):
            B[i,j] = 1

print(A)
print(B)