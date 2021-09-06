# Solution 1 using Iterative method
def sum_of_natural(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

# Solution 2 using recursion
def sum(n):
    return 0 if n == 0 else n + sum(n - 1)

print(sum_of_natural(5))
print(sum(5))