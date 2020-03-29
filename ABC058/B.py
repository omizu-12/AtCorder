O = list(input())
E = list(input())
ans = list()
LEN = len(O)+len(E)
for i in range(LEN):
    if i%2==0:
        ans.append(O[0])
        del O[0]
    else:
        ans.append(E[0])
        del E[0]
result = "".join(ans)
print(result)
