n = int(input())
nlist = list(map(int, input().split()))
m = max(nlist)
for i in range(len(nlist)):
    nlist[i] = nlist[i] / m * 100
print(round(sum(nlist) / n, 6))
