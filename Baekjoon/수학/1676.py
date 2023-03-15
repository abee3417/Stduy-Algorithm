def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)

cnt = 0
n = str(fact(int(input())))
for i in range(-1, -(len(n)+1), -1):
    if (n[i] != '0'):
        break
    cnt += 1
print(cnt)
