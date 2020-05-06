N = int(input())
S = input()
S_ans = "b"
a = "a"
b = "b"
c  ="c"

if (N-1)%2 != 0:
    print(-1)
elif N == 1:
    if S == "b":
        print(0)
    else:
        print(-1)
else:
    for i in range(1,int((N-1)/2)+1):
        if i%3 == 1:
            S_ans = a + S_ans +c 
        if i%3 == 2:
            S_ans = c + S_ans +a        
        if i%3 == 0:
            S_ans = b + S_ans +b

    if S == S_ans:
        print(int((N-1)/2))
    else:
        print(-1)