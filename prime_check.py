# Solution 1 - Iterative Method
def check_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return 0
    return 1

# Solution 2 - Recursive Method:
def prime_check(n, i = 2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if (i * i) > n:
        return True
    return prime_check(n, i + 1)

if check_prime(2):
    print("Prime Number")
else:
    print("Not Prime Number")

if prime_check(79):
    print("Prime Number")
else:
    print("Not Prime Number")