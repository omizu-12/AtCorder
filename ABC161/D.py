from collections import deque
K = int(input())
d = deque()
for i in range(1,10):
    d.append(i)
for i in range(K):
    x = d.popleft()
    y = x%10
    z = 10*x+y
    if y != 0:
        d.append(z-1)
    d.append(z)
    if y != 9:
        d.append(z+1)
print(x)



