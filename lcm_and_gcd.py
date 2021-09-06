# Solution 1
def find_lcm(a, b):
    lcm = a if a > b else b

    while(1):
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        lcm += 1

# Solution 2 using GCD
def get_lcm(a, b):
    i = 1
    while(i <= a and i <= b):
        if a % i == 0 and b % i == 0:
            gcd = i
        i += 1
    return {'gcd': gcd, 'lcm': int(((a * b) / gcd))}


print(find_lcm(8, 36))
print(get_lcm(8, 36))