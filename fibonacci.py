def fibonacci(n):
    sum = 0
    a = 0
    b = 1
    print(0, end=" ")
    print(1, end=" ")
    # using formula
    for i in range(1, n+1):
        sum = a + b
        a = b
        b = sum
        print(sum, end=" ")

# Solution 2 - Recursive method
def fib(n):
    return n if n <= 1 else (fib(n - 1) + fib(n - 2))

fibonacci(10)