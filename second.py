# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i+1

# def quickSort(arr, low, high):
#     if low < high:
#         partitionIndex = partition(arr, low, high)
#         quickSort(arr, low, partitionIndex-1)
#         quickSort(arr, partitionIndex+1, high)


def sort(arr):
    j = 0

    while j < len(arr)-1:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j = -1
        j +=1


arr = [25, 12, 1, 36, 5, 89, 21, 12]
# quickSort(arr, 0, len(arr)-1)
sort(arr)
print(arr)
print(f"Second Lowest {arr[1]} and Second Hightst {arr[len(arr)-2]}")