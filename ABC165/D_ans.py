import math
A,B,N = list(map(int,input().split()))
c = int()
if B-1 > N:
    i = N
else:
    i = B-1
c = math.floor(A*i/B)-(A*math.floor(i/B))

print(c)