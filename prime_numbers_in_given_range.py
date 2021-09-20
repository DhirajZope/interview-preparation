# Solution 1
def list_prime(start, end):
    prime = []
    for i in range(start, end+1):
        for j in range(2, i // 2):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return tuple(prime)


print(list_prime(11, 500))