N = int(input())
X = list(map(int,input().split()))
A =10**8
for i in range(100):
    temp = 0
    for j in range(N):
        temp += (X[j-1]-i)**2
    if temp < A:
        A = temp
print(A)
