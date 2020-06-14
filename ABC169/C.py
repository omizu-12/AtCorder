import numpy as np 
A,B = map(str,input().split())
A = int(A)
B = int(B[0]+B[2]+B[3])
print(int(A*B//100))
