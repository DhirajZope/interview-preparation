def check_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

def solution(n):
    combination = []
    for i in range(2, (n // 2)+1):
        if check_prime(i):
            diff = n - i
            if check_prime(diff):
                combination.append((i, diff))
    return combination


if __name__ == '__main__':
    print(solution(34))
        