def gcd(n1, n2):
    if (n2 == 0):
        return n1
    return gcd(n2, n1 % n2)

n = int(input())
s = input()
li = list(map(int, s.split()))
for i in range(1, n):
    div = gcd(li[0], li[i])
    print('{}/{}'.format(li[0]//div, li[i]//div))