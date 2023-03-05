from collections import deque
q = deque()
n, k = map(int, input().split())
q = deque([x for x in range(1, n+1)])
result = []
while (len(q) != 0):
    for i in range(k):
        tmp = q.popleft()
        if (i == (k-1)):
            result.append(tmp)
        else:
            q.append(tmp)
print('<', end='')
for i in range(n):
    if (i == (n-1)):
        print(result[i], end='>\n')
    else:
        print(result[i], end=', ')