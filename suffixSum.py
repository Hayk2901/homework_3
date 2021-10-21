seq = input().split()
print(seq)
n = len(seq)
s = 0
for i in range(n):
    s += float(seq[i])
for i in range(n):
    print(s)
    s -= float(seq[i])
