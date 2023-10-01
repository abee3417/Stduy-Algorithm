import sys
sys.setrecursionlimit(10**6)

def dfs(y, x):
    global cnt, visit
    visit[y][x] = 1
    cnt += 1
    location = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in location:
        new_y = y + i[0]
        new_x = x + i[1]
        if (graph[new_y][new_x] == '1' and visit[new_y][new_x] == 0):
            dfs(new_y, new_x)

n = int(input())
cnt = 0
result = []
graph = [[] for _ in range(n+2)]
visit = [[0 for _ in range(n+2)] for _ in range(n+2)]
graph[0] = "0" * (n+2)
for i in range(1, n+1):
    tmp = "0" + input() + "0"
    graph[i] = tmp
graph[n+1] = "0" * (n+2)
for i in range(1, n+1):
    for j in range(1, n+1):
        if (graph[i][j] == '1' and visit[i][j] == 0):
            cnt = 0
            dfs(i, j)
            result.append(cnt)
print(len(result))
for i in sorted(result):
    print(i)