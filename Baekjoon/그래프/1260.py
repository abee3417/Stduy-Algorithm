import sys
from collections import deque
n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visit = [False for i in range(n+1)]
q = deque()

# dfs 함수
def dfs(v):
    print(v, end=' ')
    visit[v] = True # 한번 방문한 곳은 방문하지 않게 한다.
    for i in graph[v]:
        if (visit[i] == False):
            dfs(i)

# bfs 함수
def bfs(v):
    q.append(v)
    visit[v] = True
    while (len(q) != 0):
        parent = q.popleft()
        print(parent, end=' ')
        for i in graph[parent]:
            if (visit[i] == False):
                q.append(i)
                visit[i] = True

# 간선 연결 작업과 정렬
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

dfs(v)
print()
# bfs 전 visit 초기화
visit = [False for i in range(n+1)]
bfs(v)