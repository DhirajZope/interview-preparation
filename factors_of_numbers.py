# Solution 1 - using list comprehension
def factors(n):
    return tuple([a for a in range(1, n+1) if n % a == 0])

# Solution 2 - using loop
def find_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    print(find_factors(15))