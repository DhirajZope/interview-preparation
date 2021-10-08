def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1    


def quickSort(arr, low, high):
    if low < high:
        partitionIndex = partition(arr, low, high)
        quickSort(arr, low, partitionIndex-1)
        quickSort(arr, partitionIndex+1, high)


if __name__ == '__main__':
    # arr = [3, 5, 2, 13, 12]
    arr = [25, 12, 1, 36, 5, 89, 21, 12]
    # arr = [21, 3, 43, 5, 65, 4, 65, 2, 1, 67, 4]
    n = len(arr)
    quickSort(arr, 0, n-1)
    print(arr)