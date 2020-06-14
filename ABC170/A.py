A = list(map(int,input().split()))
c = int() 
for i in range(5):
    if A[i] == 0:
        c = i+1
print(c)