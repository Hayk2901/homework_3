from math import sqrt

n = int(input())


def prime(k):
    m = int(sqrt(k))
    for j in range(3, m+1, 2):
        if k % j == 0:
            return False
    return True


if n == 4:
    print(2, 2)
else:
    for i in range(3, n, 2):
        if prime(i) and prime(n - i):
            print(i, n - i)
            break
