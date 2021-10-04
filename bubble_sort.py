def bubble_sort(arr):
    n = len(arr)
    # Loop to traverse the array till len(arr)-1
    for i in range(n-1):
        # Loop for comparison and swapping till len(arr)-1-i
        for j in range(n - 1 - i):
            # Swap elements.
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

if __name__ == '__main__':
    a = list(map(int, input().split()))
    print("Entered Array: ", a)
    print("Sorted Array: ", bubble_sort(a))