K,N  =list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(sorted(A))
C = list()
ans = int()

for i in range(len(B)-1):
    C.append(B[i+1]-B[i])

C.append((K-B[-1])+(B[0]))
C = sorted(C)

for i in range(N-1):
    ans += C[i]

print(ans)