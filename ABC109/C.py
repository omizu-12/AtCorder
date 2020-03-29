import fractions
N,X = map(int,input().split())
x = list(map(int,input().split()))
x.append(X)
b = list(sorted(x))
c = list()
for i in range(N):
    c.append(b[i+1]-b[i])

t = 0
for i in range(N):
    t = fractions.gcd(t, c[i])
print(t)
