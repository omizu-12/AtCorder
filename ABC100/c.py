N = int(input())
A = list(map(int,input().split()))
A2 = list(filter(lambda x: x%2==0, A))
count = 0
for i in range(len(A2)):
    while A2[i]%2 == 0:
        A2[i] /= 2
        count += 1
print(count)
