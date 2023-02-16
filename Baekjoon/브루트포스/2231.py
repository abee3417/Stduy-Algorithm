n = int(input())
exist = False
for i in range(n):
    sum, tmp = i, i
    while (tmp > 0):
        sum += tmp % 10
        tmp = tmp // 10
    if (n == sum):
        exist = True
        print(i)
        break
if (exist == False):
    print(0)