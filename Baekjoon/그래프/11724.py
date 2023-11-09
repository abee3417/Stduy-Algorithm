import sys
sys.setrecursionlimit(100000)

def dfs(n):
    global visit
    visit[n] = 1
    for i in graph[n]:
        if (visit[i] == 0):
            dfs(i)

cnt = 0
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    if (visit[i] == 0):
        cnt += 1
        dfs(i)
print(cnt)