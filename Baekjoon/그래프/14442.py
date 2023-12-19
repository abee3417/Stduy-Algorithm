#문제 2206에서 벽을 K개까지 부수는걸로 조건변경
from collections import deque
q = deque()
cnt = 0
location = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs():
    global visit, q
    while q:
        y, x, cnt, dis = q.popleft() #pre[0]:벽뿌여부, pre[1]:행, pre[2]:열, pre[3]:코스트
        if (y == n-1 and x == m-1):
            return dis
        for i in location:
            new_y = y + i[0]
            new_x = x + i[1]
            if (0 <= new_y < n and 0 <= new_x < m):
                #이동이 가능하면 벽뿌 여부에 따른 그래프 탐색을 한다
                if (graph[new_y][new_x] == '0' and visit[new_y][new_x][cnt] == 0):
                    visit[new_y][new_x][cnt] = 1
                    q.append((new_y, new_x, cnt, dis + 1))
                #이동할 수 없는 경우가 나올 경우, 딱 k번만 벽뿌를 허용한다
                elif (graph[new_y][new_x] == '1' and cnt < k and visit[new_y][new_x][cnt+1] == 0):
                    visit[new_y][new_x][cnt+1] = 1
                    q.append((new_y, new_x, cnt + 1, dis + 1))
    return -1 

n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visit = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)] #벽뿌 여부 포함한 3차원 리스트
q.append((0, 0, 0, 1)) #기존 벽뿌1 문제 입력방식에서 깔끔하게 코드 수정
visit[0][0][0] = 1
print(bfs())