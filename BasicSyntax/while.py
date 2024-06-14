# nが5から1までの数字を1つずつ減算しながら表示する

# n = 5
# while n > 0:
#     print(n)
#     n -= 1

# xが1から10までの数字を1つずつ加算ながら表示する

# x = 1
# while x <= 10:
#     print(x)
#     x += 1

# n を23から1まで減らし、5で止まり、奇数の時だけ n を出力します。
n = 23
while n > 0:
    n -= 1
    if n == 5:
        break
    if n % 2 == 0:
        continue
    print(n)

