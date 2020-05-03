N = int(input())
a = list(map(int,input().split()))
b = 1
c = 0
for i in range(N):
    if b ==a[i]:
        b += 1
    else:
        c += 1
if N == c:
    print("-1")
else:
    print(c)