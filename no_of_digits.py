# Solution 1
def digits(n):
    count = 0
    while n != 0:
        n = n // 10
        count += 1

    return count

# Solution 2 - using recursion
def no_digits(n):
    if n == 0:
        return 0
    return 1 + no_digits(n // 10)

print(digits(327))
print(no_digits(1000))