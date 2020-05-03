import math
A,B  = list(map(int,input().split()))
ans  = 1
c = 0
if B ==1:
    print("0")
elif B <= A:
    print("1")
else:
    while ans < B:
        ans += A-1
        c += 1
    print(c)