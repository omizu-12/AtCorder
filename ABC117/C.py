N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
B =  sorted(A)
C = list()
total = 0
if N >= M:
    total = 0
else:
    for i in range(M-1):
        C.append(B[i+1]-B[i])
    D = sorted(C)
    E = D[0:(M-N)]
    total = sum(E)
print(total)