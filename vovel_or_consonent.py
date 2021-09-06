# Solution 1
def check_vowel(ch):
    vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if ch in vovels:
        return 'Vovel'
    else:
        return 'consonant'

# Solution 2 using if..else statement
def is_vowel(ch):
    if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
        return 'Vovel'
    else:
        return 'Consonant'

if __name__ == '__main__':
    ch = input("Enter Character: ")[0]
    # print(check_vowel(ch))
    print(is_vowel(ch))