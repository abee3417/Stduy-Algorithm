from collections import deque
N, M = map(int, input().split())
location = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def check_0(y, x): #주변에 외부공기(0)의 수를 체크해주는 함수, 1은 기본 visit값이며 2부터가 +1개, 3은 +2개...
    li = [cheese[y][x+1], cheese[y+1][x], cheese[y][x-1], cheese[y-1][x]]
    return 1+li.count(0)

def find_inner(): #내부공기, 외부공기 구분을 위한 bfs응용함수
    global cheese, visit, cnt_0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if (cheese[i][j] == -1): #이전에 사용했던 내부공기 정보는 초기화
                cheese[i][j] = 0
    q = deque()
    q.append((1, 1))
    visit[1][1] = 1
    while (len(q) != 0):
        y, x = q.popleft()
        for i in location:
            _y, _x = y + i[0], x + i[1]
            if (not (0 < _y < N+1 and 0 < _x < M+1)): continue
            if (cheese[_y][_x] == 0 and visit[_y][_x] == 0):
                q.append((_y, _x))
                visit[_y][_x] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if (cheese[i][j] == 0): 
                cnt_0 += 1 #종료 조건을 위한 0의 갯수를 세어준다
                if (visit[i][j] == 0): #방문하지 않은 0은 내부 공기이므로 -1로 변경
                    cheese[i][j] = -1

def find_cheese(init_y, init_x): #녹을 치즈를 찾기 위한 bfs응용함수
    global cheese, visit
    q = deque()
    q.append((init_y, init_x))
    visit[init_y][init_x] = check_0(init_y, init_x)
    while (len(q) != 0):
        y, x = q.popleft()
        for i in location:
            _y, _x = y + i[0], x + i[1]
            if (not (0 < _y < N+1 and 0 < _x < M+1)): continue
            if (cheese[_y][_x] == 1 and visit[_y][_x] == 0):
                q.append((_y, _x))
                visit[_y][_x] = check_0(_y, _x)

cheese = [[0 for _ in range(M+2)] for _ in range(N+2)]
for i in range(1, N+1):
    cheese[i][1:M+1] = list(map(int, input().split()))
ans = 0
while True:
    visit = [[0 for _ in range(M+1)] for _ in range(N+1)]
    cnt_0 = 0
    find_inner()
    if (cnt_0 == N*M): break #종료조건
    visit = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if (cheese[i][j] == 1 and visit[i][j] == 0):
                find_cheese(i, j)
            if (visit[i][j] >= 3): #주위에 외부공기가 2개이상이라면 치즈를 녹힌다
                cheese[i][j] = 0
    ans += 1
print(ans)