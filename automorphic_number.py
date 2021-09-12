# A Number n is called automorphic if and only if the last digit of square if n == n
# e.g square of 5 == 25, the last digit of 25 is 5 which is equal to given digit 5 hence 5 is automorphic number.

def isAutomorphic(N) :
    sq = N * N

    if N % 10 != sq % 10:
        return False
    return True

N = int(input())
if isAutomorphic(N) :
	print ('Automorphic')
else :
	print ('Not Automorphic')
