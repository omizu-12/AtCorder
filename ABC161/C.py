import math
N,K= list(map(int,input().split()))
a = int(N/K)
a1 = a*K
a2 = (a+1)*K
if N % K ==0:
    Num = 0
else:
    if abs(N%K) < abs((N%K)-K) :
        Num = abs(N%K)
    else:
        Num =  abs((N%K)-K)
    
print(Num)

