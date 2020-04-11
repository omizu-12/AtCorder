S = input()
a = list()
count = 1
ans = ""

a.append( [ S[0] ] )
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        a[-1].append(count)
        a.append( [ S[i+1] ] )
        count = 1
    else:
        count += 1
a[-1].append(count)

for i in range(len(a)):
    ans += str(a[i][0]) + str(a[i][1])
print(ans)