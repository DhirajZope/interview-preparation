def is_perfect(n):
    sum = 0
    for i in range(1, (n//2)+1):
        if n % i == 0:
            sum += i
    return True if sum == n else False


print("Perfect Number") if is_perfect(32) else print("Not Perfect")