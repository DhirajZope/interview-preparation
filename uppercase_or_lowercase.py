# Solution 1

def check_character(ch):
    if ch >= 'a' and ch <= 'z':
        print("Lowercase")
    elif ch >= 'A' and ch <= 'Z':
        print("Uppercase")
    else:
        print("Special Character") 

# Solution 2 :- More Concise Solution

def is_upper(ch):
    if ord(ch) >= 65 and ord(ch) <= 90:
        print("Uppercase")
    elif ord(ch) >= 97 and ord(ch) <= 122:
        print("Lowercase")
    elif ord(ch) >= 48 and ord(ch) <= 57:
        print("Number")
    else:
        print("Special Character")

if __name__ == '__main__':
    ch = input("Enter Character: ")[0]
    check_character(ch)
    # is_upper(ch)
        