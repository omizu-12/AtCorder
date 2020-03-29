import math
N,M = list(map(int,input().split()))
m = 0
n = 0
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if M>1:
    m =comb(M,2)
if N>1:
    n = comb(N,2)
ans = m +n
print(ans)
