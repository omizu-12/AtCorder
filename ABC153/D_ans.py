def f(H):
    if H == 1:
        return 1
    if H > 0:
        return 2 * f(int(H/2)) + 1
 
H = input()
H = int(H)
ans = f(H)
print(ans)