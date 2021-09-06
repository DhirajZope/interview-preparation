def check_signed_integer(num):
    try:
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")
    except TypeError:
        print("Not a Number")

if __name__ == '__main__':
    check_signed_integer(1)