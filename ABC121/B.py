N,M,C = list(map(int,input().split()))
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(N)]
ans = 0
c = 0
for i in range(N):
    ans = 0
    for j in range(M):
        ans += A[i][j]*B[j]
    if 0 < ans + C:
        c += 1
print(c)
