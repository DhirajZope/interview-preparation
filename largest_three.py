# Solution 1 - using built in function
def maximum(a, b, c):
    return max([a, b, c])


# Solution 2
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(maximum(1, 2, 3))
print(largest(3, 2, 5))    