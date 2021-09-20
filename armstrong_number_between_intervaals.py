def digit(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

def armstrong(start, end):
    arm = []

    for i in range(start, end+1):
        temp = i
        sum = 0
        n = digit(i)
        while temp > 0:
            dig = temp % 10
            sum += pow(dig, n)
            temp //= 10
        if sum == i:
            arm.append(i)
    return arm

print(armstrong(100, 500))