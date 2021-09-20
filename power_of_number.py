# Solution 1
def power(n, m):
    return n ** m

# Solution 2
def power2(n, m):
    return pow(n, m)

# Solution 3
def poww(n, m):
    if m == 0:
        return 1
    return n * poww(n, m=m-1)

# Solution 4
def power_of(n, m):
    pow = 1
    for i in range(m):
        pow *= n
    return pow

if __name__ == '__main__':
    print(power_of(2, 3))