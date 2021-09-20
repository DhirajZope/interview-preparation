def add_two_fractions(a, b, c, d):
    numerator = (a * d) + (c * b)
    denominator = (b * d)
    i = 1

    while i <= numerator and i <= denominator:
        if numerator % i == 0 and denominator % i == 0:
            gcd = i
        i+=1
    return(numerator // gcd, denominator // gcd)

print(add_two_fractions(1, 3, 3, 9))