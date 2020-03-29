a = int(input())
M = list(map(int,input().split()))
b = 0
max = 0
for i, v in enumerate(M):
    if i >= a-1:
        break
    if M[i] >= M[i+1]:
        b += 1
        if max < b:
            max = b
    else:
        b = 0

print(max)