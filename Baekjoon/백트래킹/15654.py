from itertools import permutations
n, m = input().split()
n = int(n)
m = int(m)
li = list(map(int, input().split()))
result = sorted(list(permutations(li, m)))
for i in result:
    for j in i:
        print(j, end=" ")
    print("\n", end="")