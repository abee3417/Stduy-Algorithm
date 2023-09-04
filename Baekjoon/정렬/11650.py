import sys
result = []
n = int(input())
for i in range(n):
    x, y = map(int, sys.stdin.readline().strip('\n').split())
    result.append((x, y))
result = sorted(result, key=lambda x: (x[0], x[1]))
for x, y in result:
    print(x, y)