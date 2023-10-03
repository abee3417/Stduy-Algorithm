import sys
from collections import deque

q = deque()
n, m = map(int, input().split())
graph = [[0 for _ in range(m+2)] for _ in range(n+2)]
visit = [[0 for _ in range(m+2)] for _ in range(n+2)]
for i in range(1, n+1):
    graph[i][1:m] = list(map(int, sys.stdin.readline().rstrip().split()))
    try: # 2가 있는 곳을 좌표로 미리 저장
        x_2 = graph[i].index(2)
        y_2 = i
    except:
        continue
location = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우
cnt = 0 #결과표(visit)에 입력할 수
#bfs start
q.append((y_2, x_2))
visit[y_2][x_2] = cnt
while (len(q) != 0):
    new = q.popleft()
    cnt = visit[new[0]][new[1]] + 1 #자신의 좌표값+1로 설정
    for i in range(4): #자식노드4개(상하좌우) 탐색
        y_new = new[0] + location[i][0]
        x_new = new[1] + location[i][1]
        if (graph[y_new][x_new] == 1 and visit[y_new][x_new] == 0):
            q.append((y_new, x_new))
            visit[y_new][x_new] = cnt
#print
for i in range(1, n+1):
    for j in range(1, m+1):
        if (graph[i][j] == 1 and visit[i][j] == 0):
            print(-1, end=" ") #갈수없는 길은 -1로 출력
        else:
            print(visit[i][j], end=" ")
    print()