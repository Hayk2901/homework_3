n = int(input())
m = int(input())


def palindrome(k):
    s = 0
    while k != 0:
        last = k % 10
        s = s * 10 + last
        k //= 10
    return s


for i in range(n, m + 1):
    if palindrome(i) == i:
        print(i)
