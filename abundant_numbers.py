def is_abundant(n):
    sum = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            sum += i
    return True if sum > n else False


if __name__ == '__main__':
    print(is_abundant(18))