import sys
sys.setrecursionlimit(100000)

def dfs(y, x):
    global visit
    visit[y][x] = 1
    location = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우
    for i in location:
        _y = y + i[0] #새로운y
        _x = x + i[1] #새로운x
        if (graph[_y][_x] == 1 and visit[_y][_x] == 0):
            dfs(_y, _x)

t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0 for _ in range(52)] for _ in range(52)]
    visit = [[0 for _ in range(52)] for _ in range(52)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[y+1][x+1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (graph[i][j] == 1 and visit[i][j] == 0): #그래프상 1이고 방문X인 노드일때 dfs시작
                dfs(i, j)
                cnt += 1 #인접노드 모두 탐색시 +1
    print(cnt)