import math
X = int(input())
ans = 100
c = int(0)
while ans < X:
    ans +=  math.floor(ans*0.01)
    c += 1
print(c)