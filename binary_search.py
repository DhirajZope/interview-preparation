# Sort Array Using Insertion sort
def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Binary Sort Searching Algorithm
def binary_search(arr, key):
    arr = sort(arr)
    print(f"Sorted Array {arr}")
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Driver Function
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    key = int(input("Enter element to search: "))
    result = binary_search(arr, key)
    print(f"Found at index {result}") if result else print("Not Found")

a = [2, 4, 3, 2, 1, 6, 7]
