nlist = []
max = 0
index = 0
for i in range(9):
    nlist.append(int(input()))
for i in range(9):
    if (max < nlist[i]):
        max = nlist[i]
        index = i + 1
print(max)
print(index)