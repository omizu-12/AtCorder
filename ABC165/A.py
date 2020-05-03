import math
K = int(input())
A,B = list(map(int,input().split()))
num = 0
while num <=2000:
    num += K
    if num >1000:
        print("NG")
        break
    if num <= B and A <= num:
        print("OK")
        break
    else:
        continue

