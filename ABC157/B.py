A = [list(map(int,input().split())) for i in range(3)]
N = int(input())
B = [list(map(int,input().split())) for i in range(N)]
for k in range(N):
    for i in range(3):
        for j in range(3):
            if B[k][0] == A[i][j]:
                A[i][j] = 0

if A[0][0] == A[0][1] == A[0][2] ==0:
    print("Yes")
elif A[1][0] == A[1][1] == A[1][2] ==0:
    print("Yes")
elif A[2][0] == A[2][1] == A[2][2] ==0:
    print("Yes")
elif A[0][0] == A[1][0] == A[2][0] ==0:
    print("Yes")
elif A[0][1] == A[1][1] == A[2][1] ==0:
    print("Yes")
elif A[0][2] == A[1][2] == A[2][2] ==0:
    print("Yes")
elif A[0][0] == A[1][1] == A[2][2] ==0:
    print("Yes")
elif A[0][2] == A[1][1] == A[2][0] ==0:
    print("Yes")
else:
    print("No")
