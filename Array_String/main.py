# Search
def search(arr: int[], target: int, length: int):
    for i in range(length):
        if arr[i] == target:
            return i
    return -1

# Insert
def insert(arr: int[], index: int, value: int, length: int):
    # 最後の要素からindexまで右シフトする
    for i in range(length-1, index-1, -1):
        arr[i+1] = arr[i]
    arr[index] = value
