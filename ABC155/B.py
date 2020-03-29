N = int(input())
M = list(map(int,input().split()))
X = [i for i in M if i % 2 == 0]
Y = [i for i in X if i % 3 ==0 or i % 5 ==0]

if len(X) == len(Y):
    print("APPROVED")
else:
    print("DENIED")