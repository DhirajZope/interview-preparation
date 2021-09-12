# a harshad number (or Niven number) in a given number base is an integer 
# that is divisible by the sum of its digits when written in that base.
# e.g 6804 = sum of digits of 6 + 8 + 0+ 4 = 18
# 6804 / 18 == 37 or 6804 % 18 == 0 hence 6804 is harshad number.

# Iterative sum of digit function
def sum_of_digits(n):
    sum = 0
    while n > 0:
        dig = n % 10
        sum += dig
        n = n // 10
    return sum

# resursive sum_of_digits function 
def digisum(n, sum=0):
    return sum if n <= 0 else sum + digisum(n // 10, n % 10)
print(digisum(225))


def is_harshad_number(n):
    if n % sum_of_digits(n) == 0:
        return True
    return False

print("Harshad Number") if is_harshad_number(378) else print("Not Harshad Number")