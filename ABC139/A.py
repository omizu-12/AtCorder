a = list(str(input()))
b = list(str(input()))
count = 0
for i in range(3):
    if a[i-1] == b[i-1]:
        count +=1
print(count)