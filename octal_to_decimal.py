# Solution 1
def decimal(n):
    decimal = 0
    i = 0
    while n > 0:
        rem = n % 10
        decimal += rem * (8 ** i)
        i += 1
        n //= 10
    return decimal

# Solution 2
print(int('67', 8))
print(decimal(67))