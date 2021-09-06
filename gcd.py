# Solution 1
def find_gcd(a, b):
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

# Solution 2 - Recursive Method
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    
    if a > b:
        return gcd(a- b, b)
    else:
        return gcd(a, b - a)

print(find_gcd(8, 36))
print(gcd(20 , 17))