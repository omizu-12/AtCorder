N,T = map(int,input().split())
A = [int(input())for i in range(N)]
ans = T
for i in range(N-1):
    if A[i+1] - A[i] <= T:
        ans +=  A[i+1] - A[i]
    else:
        ans += T
print(ans)
