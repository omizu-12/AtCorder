H,N = list(map(int,input().split()))
X = list(map(int,input().split()))
a = H
for i in range(N):
    a -= X[i-1]
if a > 0:
    print("No")
else:
    print("Yes")