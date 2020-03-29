O = list(input())
E = list(input())
ans = list()
 
for i in range(len(O)):
    ans.append(O[i])
    if len(E) > i:
        ans.append(E[i])
result = "".join(ans)
print(result)