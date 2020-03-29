N,K = list(map(int,input().split()))
per = 0
def f(x,y):
    count = 0
    while (x < y):
        x = 2*x
        count += 1
    return count

for i in range(N):
    b = int(f(i+1,K))
    per += (1/N)*((1/2)**b)
print(per)