import sys
n, m = input().split()
n = int(n)
m = int(m) 
poke = {}
for i in range(1, n+1):
    poke[str(i)] = sys.stdin.readline().rstrip()
rev_poke = {value : key for key, value in poke.items()}
for i in range(m):
    tmp = sys.stdin.readline().rstrip()
    if (not 'A' <= tmp[0] <= 'z'):
        print(poke[tmp])
    else:
        print(rev_poke[tmp])