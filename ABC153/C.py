N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
B = sorted(A)
if N <= K:
    print(0)
else:
    for i in range(K):
        B.pop(-1)

    print(sum(B))