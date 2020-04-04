N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
list.sort(A,reverse=True)
count = 0
Sum = sum(A)
for i in range(M):
    if A[i] >= Sum/(4*M):
        count +=1

if M ==count:
    print("Yes")
else:
    print("No")