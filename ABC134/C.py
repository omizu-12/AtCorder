import copy
N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
B = sorted(A)

a_max = max(A)
count = A.count(a_max)
for i in range(N):
    if A[i] < a_max and count >= 2:
        print(a_max[0])
    else:
        print(B[-2][0])
