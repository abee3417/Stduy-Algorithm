import sys
from collections import deque

q = deque() #bfs 전용 큐
info_1 = deque() #1의 위치 갱신을 위한 큐
m, n, h = map(int, input().split())
graph = [[[-1 for _ in range(m+2)] for _ in range(n+2)] for _ in range(h+2)]
visit = [[[-1 for _ in range(m+2)] for _ in range(n+2)] for _ in range(h+2)]
for H in range(1, h+1):
    for i in range(1, n+1):
        graph[H][i][1:m+1]  = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(1, m+1):
            if (graph[H][i][j] == 1): #첫 1이있는 좌표들을 체크
                visit[H][i][j] = 1
                info_1.append([H, i, j])
                q.append([H, i, j])
location = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
result = 0 #결과값(Day)
while True:
    count_1 = len(info_1)
    for _ in range(count_1): #탐색 안한 토마토위치 전부 bfs
        new = q.popleft()
        info_1.popleft()
        for i in range(6): #자식노드6개 탐색
            z_new = new[0] + location[i][0]
            y_new = new[1] + location[i][1]
            x_new = new[2] + location[i][2]
            if (graph[z_new][y_new][x_new] == 0 and visit[z_new][y_new][x_new] != 1):
                info_1.append([z_new, y_new, x_new])
                q.append([z_new, y_new, x_new])
                visit[z_new][y_new][x_new] = 1
    if (len(q) == 0 or len(info_1) == 0): break
    result += 1
for H in range(1, h+1):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (graph[H][i][j] == 0 and visit[H][i][j] == -1):
                result = -1 #모두 익은 토마토로 못만든걸 체크하면 -1
                break
print(result)