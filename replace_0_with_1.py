def replace(n):
    if n == 0:
        return 0
    digit = n % 10
    if digit == 0:
        digit = 1
    return replace(n // 10) * 10 + digit

print(replace(20002))