# Solution 1 - Using Iterative Method
def rev(n):
    rev = 0
    while n > 0:
        dig = n % 10
        rev = (rev * 10) + dig
        n = n // 10

    return rev

def is_palindrome(n):
    if n == rev(n):
        return True
    else:
        return False

# Solution 2 - Recursive Method
def palindrome(n, rev = 0):
    if n > 0:
        rev = (rev * 10) + (n % 10)
        return palindrome(n // 10, rev)
    return rev

print("Palindrome") if is_palindrome(232) else print("Not Palindrome")
n = 4234324876
print("Palindrome") if n == palindrome(n) else print("Not Palindrome")