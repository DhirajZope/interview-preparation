from binary_to_decimal import decimal

def binary_to_octal(n):
    n = decimal(n)
    # print(n)
    i = 0
    octal = 0

    while n > 0:
        rem = n % 8
        octal += rem + pow(8, i)
        n //= 8
        i += 1
    return octal

print(binary_to_octal(1111))
# binary_to_octal(1010101)