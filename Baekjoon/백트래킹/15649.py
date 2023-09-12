from itertools import combinations
n, m = input().split()
n = int(n)
m = int(m)
li = []
for i in range(1, n+1):
    li.append(i)
result = list(combinations(li, m))
for i in result:
    for j in i:
        print(j, end=" ")
    print("\n", end="")