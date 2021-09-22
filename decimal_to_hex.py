def hexadecimal(n):
    values = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    hexa = ''
    while n > 0:
        rem = n % 16
        if rem < 10:
            hexa += str(rem)
        else:
            hexa += values[rem]
        n //= 16
    return hexa[::-1]

print(hexadecimal(7562))

# Solution 2
print(hex(7562).replace('0x', ''))
