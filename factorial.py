# Solution 1 - Iterative Method
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

# Solution 2 - REcursive Method
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(factorial(5))
print(fact(1))