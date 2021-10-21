n = int(input())
k = int(input())
num = []

k %= n
for i in range(n):
    num.append(int(input()))
for i in range(n-k, n):
    print(num[i])
for i in range(n-k):
    print(num[i])
