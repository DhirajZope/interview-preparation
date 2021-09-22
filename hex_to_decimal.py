def hexadecimal(n):
    values = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15
    }
    power = len(n)-1
    dec = 0

    for ch in n.upper():
        dec += values[ch] * (16 ** power)
        power -= 1
    return dec


    


print(hexadecimal('A'))
print(int('A', 16))
