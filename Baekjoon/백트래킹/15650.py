from itertools import permutations
n, m = input().split()
n = int(n)
m = int(m)
li = []
for i in range(1, n+1):
    li.append(i)
result = list(permutations(li, m))
for i in result:
    for j in i:
        print(j, end=" ")
    print("\n", end="")