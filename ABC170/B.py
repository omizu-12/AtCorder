X,Y = map(int,input().split())

if Y <= X*4 and X*2 <= Y and Y%2 ==0:
    print("Yes")
else:
    print("No")