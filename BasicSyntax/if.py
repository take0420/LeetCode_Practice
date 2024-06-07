# 修正後の例
# nが5より大きい場合、positive
# nが0未満の場合、negative
# nが0の場合、zero

n = 5

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

# 'and' 演算子の使用
# 'or' 演算子の使用
# 'not' 演算子の使用
# Pythonでは範囲を条件にする時に以下のようにできます

x, y = 5, 10
if x > 0 and y > 0:
    print("Both n and m are positive.")

x = -5
if x < 0 and y > 0:
    print("Either x is positive or y is negative.")

if not x > 0:
    print("x is not positive.")

if 0 < x < 10:
    print("n is between 0 and 10")
