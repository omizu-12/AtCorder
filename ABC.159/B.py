s = list(input())
N = int(len(s))
a = int(((N-1)/2))
b = int(((N+3)/2))
s1 = s[0:a]
s2 = s[b:N-1]
if s1 == list(reversed(s1)) and s2 ==list(reversed(s2)) and s ==list(reversed(s)):
    print("Yes")
else:
    print("No")