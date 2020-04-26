A,B,C,D = list(map(int,input().split()))

count1 = 0
count2 = 0
while A > 0:
    A -= D
    count1 += 1
while C > 0:
    C -= B
    count2 += 1

if count1 < count2:
    print("No")
else:
    print("Yes")