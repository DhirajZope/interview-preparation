def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    for k in range(low, high):
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr, low, high):
    if low < high:
        partitionIndex = partition(arr, low, high)
        quickSort(arr, low, partitionIndex-1)
        quickSort(arr, partitionIndex+1, high)

if __name__ == '__main__':
    arr = [21,2,36,12,2,38,95,1]
    high = len(arr)-1
    quickSort(arr, 0, high)
    print(arr)