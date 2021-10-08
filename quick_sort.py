def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    # print(f"Low {low}")
    # print(f"High {high}")

    while i < j:
        # print(arr)
        # print("Pivot", pivot)
        # print("i ",i)
        # print("j ", j)
        while arr[i] <= pivot:
            i += 1
            # print("Under i", i)
        while arr[j] > pivot:
            j -= 1
            # print("Under j", j)

        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    # print("Final", arr)
    return j
    


def quickSort(arr, low, high):
    if low < high:
        partitionIndex = partition(arr, low, high)
        quickSort(arr, low, partitionIndex-1)
        quickSort(arr, partitionIndex+1, high)


if __name__ == '__main__':
    # arr = [3, 5, 2, 13, 12]
    arr = [25, 12, 1, 36, 5, 89, 21, 12]
    n = len(arr)
    quickSort(arr, 0, n-1)
    print(arr)