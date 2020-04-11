N  =int(input())
A = [list(map(int,input().split()))for i in range(N)]
count=int(0)
l = [0] * 100000

for i in range(N):
	a = int(A[i][0])
	l[a-1] += 1
for i in range(max(A)):
	n = int(l[i])
	if n > 1: count += n - 1
print(count)