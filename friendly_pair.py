def is_friendly(num1, num2):
    sum1 = sum2 = 0
    for i in range(1, (num1//2)+1):
        if num1 % i == 0:
            sum1 += i
    for i in range(1, (num2//2)+1):
        if num2 % i == 0:
            sum2+= i
    if (sum1 == num1) and (sum2 == num2):
        return True
    return False

print("Friendly Pair") if is_friendly(6, 28) else print("Not Friendly")

