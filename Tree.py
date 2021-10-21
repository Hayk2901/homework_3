n = int(input())
string = []
k = (n-1) // 2

for i in range((n-1)//2+1):
    for j in range(k):
        string.append(' ')
    for g in range(n-2*k):
        string.append('*')
    print(''.join(string))
    k -= 1
    string = []
