def ascii(ch):
    try:
        return(ord(ch))
    except (TypeError, ValueError) as e:
        print(e)
        return "Not a Character"

if __name__ == '__main__':
    print(ascii('6'))