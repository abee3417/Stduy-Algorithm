#문제 2178에서 업그레이드한 코드
from collections import deque
q = deque()
cnt = 0
location = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs():
    global visit, q
    while (len(q) != 0):
        pre = q.popleft() #pre[0]:벽뿌여부, pre[1]:행, pre[2]:열, pre[3]:코스트
        if (pre[1] == n and pre[2] == m):
            return pre[3]
        for i in location:
            new_y = pre[1] + i[0]
            new_x = pre[2] + i[1]
            #이동이 가능하면 벽뿌 여부에 따른 그래프 탐색을 한다
            if (graph[new_y][new_x] == '0' and visit[pre[0]][new_y][new_x] == 0):
                visit[pre[0]][new_y][new_x] = 1
                if (pre[0] == 0):
                    q.append((0, new_y, new_x, pre[3] + 1))
                else:
                    q.append((1, new_y, new_x, pre[3] + 1))
            #이동할 수 없는 경우가 나올 경우, 딱 1번만 벽뿌를 허용한다
            elif (graph[new_y][new_x] == '1' and pre[0] == 0 and visit[pre[0]][new_y][new_x] == 0):
                visit[pre[0]][new_y][new_x] = 1
                q.append((1, new_y, new_x, pre[3] + 1))
    return -1 

n, m = map(int, input().split())
graph = [[] for _ in range(n+2)]
visit = [[[0 for _ in range(m+2)] for _ in range(n+2)] for _ in range(2)] #벽뿌x를 0, 벽뿌완료를 1로 설정한 3차원 리스트
graph[0] = "*" * (m+2)
for i in range(1, n+1):
    tmp = "*" + input() + "*"
    graph[i] = tmp
graph[n+1] = "*" * (m+2)
q.append((0, 1, 1, 1))
visit[0][1][1] = 1
print(bfs())