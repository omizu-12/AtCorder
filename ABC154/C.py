N = input()
M = list(map(int,input().split()))
X = set(M)
Y = len(X)
Z = len(M)
if Y == Z:
    print("YES")

else:
    print("NO")
