N = int(input())
M = list(map(int,input().split()))
X = sorted(M)
for i, v in enumerate(X):
    if i >= N-1:
        break
    else:
        a = X[i]+X[i+1]
        b = a/2
        X[i+1]= a/2

print(b)