n = int(input())
result = 0
if (n < 100):
    result = n
else:
    result = 99
    for i in range(100, n+1):
        judg = True
        li = list(map(int, list(str(i))))
        dif = li[1] - li[0]
        for j in range(1, len(li)-1):
            if (li[j+1] - li[j] != dif):
                judg = False
        if (judg == True):
            result += 1
print(result)