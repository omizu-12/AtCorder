import math
A,B = list(map(int,input().split()))

for i in range(1009):
    a = math.floor((i+1)*0.08)
    b = math.floor((i+1)*0.1)
    if  a==A and b==B:
        print(i+1)
        break
    elif i == 1008:
        print("-1")