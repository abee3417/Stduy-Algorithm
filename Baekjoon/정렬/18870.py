n = int(input())
li = list(map(int, input().split()))
cmp = sorted(set(li))
dic = {cmp[i] : i for i in range(len(cmp))}
for i in li:
    print(dic[i], end=" ")