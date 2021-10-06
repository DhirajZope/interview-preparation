# Solution 1 - Using 3rd varianble
def swap(n1, n2):
    temp = n1
    n1 = n2
    n2 = temp
    print(n1, n2)

# Solution 2 without using 3rd variable addition and substraction method
def swap_two(n1, n2):
    n1 = n1 + n2
    n2 = n2 - n1
    n1 = n2 - n1
    print(n1, n2)

# Solution 3 - without using 3rd variable multiplication and division method
def swapping(n1, n2):
    n1 = n1 * n2
    n2 = n1 / n2
    n1 = n1 / n2
    print(int(n1), int(n2))

# Solution 4 - Using bitwise operator without using 3rd variable
def swapp(n1, n2):
    n1 = n1 ^ n2
    n2 = n1 ^ n2
    n1 = n1 ^ n2
    print(n1, n2)

# Solution 5
def swapTwo(n1, n2):
    n1, n2 = n2, n1
    print(n1, n2)

# swap(2, 3)
# swap_two(6, 4)
# swapping(2, 3)
swapp(8, 3)