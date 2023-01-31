nlist = list(map(int, input()))
nlist.sort(reverse=True)
print(''.join(str(s) for s in nlist))