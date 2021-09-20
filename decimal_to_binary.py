# Solution 1 - using built-in method
def binary(n):
    return bin(n)

# Solution 2
def decimal_to_binary(n):
    binary = 0
    i = 1
    while n > 0:
        rem = n % 2
        binary += rem * i
        n //= 2
        i *= 10
    return binary

print(decimal_to_binary(11))