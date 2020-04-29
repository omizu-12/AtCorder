import math
n = int(input())
S1 = 0
S2 = 0
M1 = 0
M2 = 0
Ab2 =0
ans = int(10**7)
for i in range(1,334):
    for j in range(1,334):
        #i*jの面積
        #余ったタイルの数 + 縦と横の長さの差の絶対値
        S = n - i*j + abs(i-j)
        if  S < ans and 0 <= n -i*j:
            ans = S

print(ans)

    

