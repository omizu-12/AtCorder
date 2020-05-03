S = input()

a = S.index("A")
b = [i for i, x in enumerate(S) if x == 'Z']
c = 0
for i in range(len(b)):
    if c <= b[i]:
        c  = b[i]
print(c-a+1)