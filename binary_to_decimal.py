# Solution 1
def decimal(n):
    po = 0
    sum = 0 
    while n > 0:
        dig = n % 10
        sum += pow((dig * 2), po)
        n //= 10
        po += 1
    return sum

# Solution 2 - using built in function
print(int('1011', 2))

print(decimal(1111))