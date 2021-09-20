# Solution 1
def octal(n):
    octal = 0
    i = 1
    while n > 0:
        rem = n % 8
        octal += rem * i
        n //= 8
        i *= 10
    return octal

# Solution 2 - using in-built method
print(oct(200))
print(octal(200))