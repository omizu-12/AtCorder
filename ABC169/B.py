N = int(input())
A = list(map(int,input().split()))
total = 1
if 0 < A.count(0):
    print(0)
else:
    for i in range(N):
        total *= A[i]
        if 10 ** 18 < total:
            break
    if 10**18 < total:
        print("-1")
    else:
        print(total)