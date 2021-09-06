# Solution 1 - Iterative approach
def sum_of_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum

# Solution 2 - Recursive approach
def dig_sum(n):
    return 0 if n == 0 else (n % 10) + dig_sum(n // 10)

print(sum_of_digits(123))
print(dig_sum(12345))