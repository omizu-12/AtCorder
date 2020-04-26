N = int(input())
S = input()
max = 0
for i in range(1,N):
    S1 = S[0:i]
    S2 = S[i:N]
    print("S:"+S+"S1:"+S1+"S2:"+S2)
    if len(set(S1)&set(S2)) > max:
        max = len(set(S1)&set(S2))
print(max)