# 変数の宣言と再代入
n = 0
print(n) # Output: 0

n = "ABC"
print(n) # Output: ABC

# 複数変数への1行での代入
a, b = 1, 2
print(a, b) # Output: 1, 2

# 変数のスワップ
a, b = 1, 2
a, b = b, a
print(a, b) # Output: 2, 1

# 複数変数への一括代入
a = b = c = 0
print(a, b, c) # Output: 0 0 0

# Increment, Decrement
n = 0
n += 1
print(n) # Output: 1
n -= 1
print(n) # Output: 0

# None (NULL)
n = None
print(n) # Output: None
