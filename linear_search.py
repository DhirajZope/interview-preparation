def search(arr, key):
    for i in range(len(arr)):
        # print(arr[i])
        if arr[i] == key:
            return i
    else:
        return False


arr = [43, 32, 12, 88, 4, 3]
a = search(arr, 12)
if a:
    print(f"key is found at position {a}")
else:
    print("Not found")
