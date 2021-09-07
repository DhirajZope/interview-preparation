def count_dig(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

# or - using resursive
# def dig_count(n, count = 0):
#     if n <= 0:
#         return count
#     return dig_count(n // 10, count + 1)

def is_armstrong(n):
    power = count_dig(n)
    sum = 0
    temp = n
    
    while temp > 0:
        dig = temp % 10
        sum += (dig**power)
        temp //= 10

    return True if sum == n else False

if is_armstrong(1634):
    print("Armstrong Number")
else:
    print("Not Armstrong")