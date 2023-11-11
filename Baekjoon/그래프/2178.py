from collections import deque

n, m = map(int, input().split())
cnt = 0
result = []
graph = [[] for _ in range(n+2)]
visit = [[0 for _ in range(m+2)] for _ in range(n+2)]
graph[0] = "0" * (m+2)
for i in range(1, n+1):
    tmp = "0" + input() + "0"
    graph[i] = tmp
graph[n+1] = "0" * (m+2)
location = [[0, 1], [1, 0], [0, -1], [-1, 0]]
q = deque()
q.append((1, 1, 1))
visit[1][1] = 1
while (len(q) != 0):
    pre = q.popleft()
    if (pre[0] == n and pre[1] == m):
        print(pre[2])
        break
    for i in location:
        new_y = pre[0] + i[0]
        new_x = pre[1] + i[1]
        if (graph[new_y][new_x] == '1' and visit[new_y][new_x] == 0):
            q.append((new_y, new_x, pre[2] + 1))
            visit[new_y][new_x] = 1