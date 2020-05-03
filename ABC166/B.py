import itertools
N,K = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(K*2)]
B = list()
for i in range(1,K*2+1,2):
    B.append(A[i])
C = set(list(itertools.chain.from_iterable(B)))

print(N-len(C))