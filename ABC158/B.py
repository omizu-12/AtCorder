N,A,B = list(map(int,input().split()))

C = A+B
D = int(N/C)
E = A*D
F = N%C

if F>A:
    print(E+A)
else:
    print(E+F)
