import string
# Solution 1
def is_alphabet(ch):
    alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase) 
    return True if ch in alphabets else False


# Solution 2
def check_alpha(ch):
    ch = str(ch)
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        return True
    return False

# Solution 3
def is_alpha(ch):
    ch = str(ch)[0]
    if (ord(ch) >= 97 and ord(ch) <= 122) or(ord(ch) >= 65 and ord(ch) <= 90):
        return True
    return False

    
if __name__ == '__main__':
    print(is_alpha('dhi'))