N = int(input())
S = input()
ans  = list()
for i in range(N-1):
    if not S[i] == S[i+1]:
        ans.append(S[i])
ans.append(S[-1])
A = "".join(ans)
print(len(A))