def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def is_strong(n):
    sum = 0
    temp = n
    while temp > 0:
        dig = temp % 10
        sum += factorial(dig)
        temp //= 10

    return True if sum == n else False

print("Strong Number") if is_strong(123) else print("Not Strong Number")