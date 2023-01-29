nlist = {}
for i in range(1,9):
    nlist[int(input())] = i
# 딕셔너리 key기준 정렬
nlist = dict(sorted(nlist.items()))
keys = list(nlist.values())[3:]
print(sum(list(nlist.keys())[3:]))
for i in sorted(keys):
    print(i, end=' ')