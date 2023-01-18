result = []
nlist = []
while True:
    nlist = list(map(int, input().split()))
    if (nlist.count(0) == 3):
        break
    nlist.sort()
    if (nlist[0] ** 2 + nlist[1] ** 2 == nlist[2] ** 2):
        result.append('right')
    else:
        result.append('wrong')
for i in result:
    print(i)
    