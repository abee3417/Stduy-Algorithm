from itertools import combinations_with_replacement
n, m = map(int, input().split())
ans = list(combinations_with_replacement([i for i in range(1, n+1)], m))
for i in ans:
    for j in i:
        print(j, end=" ")
    print()