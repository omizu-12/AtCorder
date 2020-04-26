h, w = map(int, input().split())
a = [''] * h
for i in range(h):
	a[i] = input() # 行の文字列

# 4 4
# ##.#
# ....
# ##.#
# .#.#
row = [False] * h # 行の出力フラグ
# => row = [ False, False, False, False ] : その行には黒色がない : False, １つでもその行に黒色がある : True
col = [False] * w # 列の出力フラグ
# => col = [ False, False, False, False ] : その列には黒色がない : False, １つでもその列に黒色がある : True

# i行目と j列目に 黒色があるかどうかを判定
for i in range(h):
	for j in range(w):
		if a[i][j] == '#': # (i, j) に黒がある = i行目に黒がある and　j列目に黒がある
			row[i] = True # i 行目に黒があるフラグを立てる
			col[j] = True # j 列目に黒があるフラグを立てる

# => row = [ True, False, True, True ] : その行には黒色がない : False, １つでもその行に黒色がある : True
# => col = [ True, True, False, True ] : その列には黒色がない : False, １つでもその列に黒色がある : True

# 結果を出力する
for i in range(h): # 何行目に黒があるか探す
	if row[i] == True: # i 行目に黒があった場合
		for j in range(w): # 何列目に黒があるか探す
			if col[j] == True: # j 列目に黒があった場合
				print(a[i][j], end = '') # 出力
		print()
# .#..
# ....
# ##.#
# .#..
# ======
# .#.
# ###
# .#.


# H, W = map(int, input().split())
# S = [input() for i in range(H)]
# S1 = [] #num
# S2 = [] #ans
# for i in range(H):
#     for i in range(W):
#         if S[i][j] == ".":
#             S1[i][j].append(1)
#         else:
#             S1[i][j].append(0)
# for i in range(W):
#     sum
# # 3 4
# # .... (0,0 => 1), (0,1 => 1), (0,2 => 1), (0,3 => 1)
# # ##.# (1,0 => 0), (1,1 => 0), (1,2 => 1), (1,3 => 0)
# # .... (0,0 => 1), (0,1 => 1), (0,2 => 1), (0,3 => 1)

# # result = [
# # 	[1, 1, 1, 1],
# # 	[0, 0, 1, 0],
# # 	[1, 1, 1, 1],
# # ]

# # result[i][j] != 1: print(result[i][j])

# # step.1 削除される行を探索
# # step.2 削除される列を探索
# # step.3 削除しない座標だけ出力

# for i in range(len(S)):
	
#     for j in range(W):
#         if S[i:len(S)][j] =".":
#             del

