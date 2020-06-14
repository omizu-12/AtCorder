import math 
X, N = map(int,input().split())
d = int(999)
d1 = int()
ans = int(999)
if 0 < N:
    P = list(map(int,input().split()))
    for i in range(999):
        if P.count(i) == 0:
            d1 = abs(X-i)
            if d1 < d and 0 <= d1:
                d = d1
                ans = i
    print(ans)
else:
    print(X)



