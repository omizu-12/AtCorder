a = [input() for i in range(3)]
x,y = map(str,a[0].split())
b,c = map(int,a[1].split())
if x == a[2]:
    b -= 1
    print(b,c)
else:
    c -= 1
    print(b,c)