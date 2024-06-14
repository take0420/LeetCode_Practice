# 0から5までの数を順に出力
# for i in range (6):
#     print(i)

# 2から4までの数を順に出力します。
# for i in range (2, 5):
#     print(i)

# 5から2までの数を逆順に出力します。
# for i in range (5, 1, -1):
#     print(i)

# 4から0までの数を逆順に出力します。
# for i in reversed(range(5)):
#     print (i)

# 0から10までの数を順に出力し、5になったらループを抜ける
for i in range (11):
    if i == 5:
        break
    print(i)

# 0から10までの奇数を順に出力します
for i in range (11):
    if i % 2 == 0:
        continue
    print(i)

# 0から5までの数を順に出力し、最後に 'done' を出力します
for i in range (6):
    print(i)
else:
    print("done")

# 0から2までの数を順に出力し、3になったらループを抜けて 'done' は出力しません
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("done")
