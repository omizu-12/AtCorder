H, W = map(int, input().split())
S = [input() for i in range(H)]
count = 0
for i in range(H):
    for j in range(W):

        # デフォルトが白色のキャンバスにおいて、square1001君は指定の場所を 黒色にしたい。
        # しかし、 "." の場合はキャンバスを白色 に染めるという操作のため、スキップして問題ない
        if S[i][j] == ".": continue

        # 黒色に染めたい場所がある（S[i][j] == "#"）時は、
        # 上下左右のマスを調べて、１つでも "#" があれば良い（上下左右に隣接する 2つのマスを選び黒く塗らなくてはならないから）

        # 左、上、右、下
        # ex. (1,1)
        # (0,1), (1,2), (2,1), (1,0)
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        is_exist = False

        # H = 1, W = 10
        # . . . . . . . # # #
        # => "Yes"
        # (x,y)
        # (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)
        # 上と下は定義されていないので範囲外
        # (0, 0)は左が範囲外、(10,0)は右が範囲外
        # [ ['...'], ['###'] ]
        # i = 0, j = 0 => '...' S[i][j][0], S[i][j][1]


        for dir in range(4):
            x = i + dx[dir] # x座標
            y = j + dy[dir] # y座標

            # (0, 1)や(1,0)だと (-1,1)や(1,-1) で範囲外を見てしまうので、そこはスキップさせる
            if x < 0 or y < 0 or H <= x or W <= y: continue
            if S[x][y] == "#": is_exist = True
        
        # ある場所 (x, y) の上下左右に黒色に染めたいマスがなかった場合、条件を満たさないため No を出す
        if is_exist == False:
            print("No")
            exit(0) # プログラムを強制終了
print("Yes")

        # if H == 1 or W == 1:
        #     if i == 0 and H == 1 and S[i][j] != S[i][j+1]:
        #         count += 1
        #     elif j == 0 and W == 1 and S[i][j] != S[i+1][j]:
        #         count += 1
        # elif H >= j-2 and W >= i-2:
        #     if S[i][j] != S[i][j+1] or S[i][j] != S[i+1][j]:
        #         count += 1

# if count == 0:
#     print("Yes")
# else:
#     print("No")