import sys
from collections import deque
cnt = 0
n = int(input())
graph = [[] for i in range(n+1)]
visit = [False for i in range(n+1)]
q = deque()
m = int(input())

# 간선 연결 작업과 정렬
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

# bfs, 1부터 시작
q.append(1)
visit[1] = True
while (len(q) != 0):
    parent = q.popleft()
    for i in graph[parent]:
        if (visit[i] == False):
            cnt += 1
            q.append(i)
            visit[i] = True

print(cnt)