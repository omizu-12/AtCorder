a = int(input())
M = []
for i in range(a):
    if i % 2 ==0:
        M.append(i)
b = len(M)
print(b/a)