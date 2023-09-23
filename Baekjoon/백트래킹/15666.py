from itertools import combinations_with_replacement
n, m = map(int, input().split())
li = sorted(set(map(int, input().split())))
ans = sorted(list(combinations_with_replacement(li, m)))
for i in ans:
    for j in i:
        print(j, end=" ")
    print()