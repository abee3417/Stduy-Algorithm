from collections import deque
import heapq
NONE = (-999, -999, -999)

def bfs():
    global graph
    visit = [[0 for _ in range(N)] for _ in range(N)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    base_y, base_x = start[1], start[2]
    graph[base_y][base_x] = 0 #시작위치를 9에서 0으로 변경 (지나갈 수 있게끔)
    visit[base_y][base_x] = 1
    q = deque()
    q.append(start)
    h = [] #우선순위에 따라 물고기를 먹으러 갈 경로를 하나만 정해야 하므로 heapq가 필요하다
    while q:
        t, y, x = q.popleft()
        for my, mx in move:
            next_y, next_x = y + my, x + mx
            if (not (0 <= next_y < N and 0 <= next_x < N)): continue
            if (0 < graph[next_y][next_x] < lv and visit[next_y][next_x] == 0): #물고기를 먹는경우
                heapq.heappush(h, (t+1, next_y, next_x)) #이렇게 heapq에 넣으면 t가작은순 -> y가작은순(위쪽) -> x가작은순(왼쪽)으로 우선순위가 정해진다
                visit[next_y][next_x] = 1
            elif ((graph[next_y][next_x] == 0 or graph[next_y][next_x] == lv) and visit[next_y][next_x] == 0): #지나갈 수 있는 경우
                q.append((t+1, next_y, next_x))
                visit[next_y][next_x] = 1
    if (len(h) != 0): #탐색을 모두 끝내면 가장 조건에 맞는 물고기 섭취 위치 정보를 리턴한다
        return h[0]
    else: #물고기 섭취 위치가 없다면 NONE을 반환, 그러면 아래 while loop이 종료된다
        return NONE

N = int(input())
graph = []
for y in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    try:
        x = tmp.index(9)
        start = (0, y, x) #다음 물고기를 먹는데 걸린시간 t, 좌표 y, x
    except:
        continue
ans, lv, exp = 0, 2, 0
while True:
    tmp = bfs()
    if (tmp == NONE): break #더 먹을 물고기가 없을 시
    time, next_y, next_x = tmp
    exp += 1 #물고기 하나 섭취
    ans += time #시간 1초 증가
    if (exp == lv): #레벨, 경험치 초기화작업
        lv += 1
        exp = 0
    start = (0, next_y, next_x) #다음 물고기를 먹기 위해 start를 현재 위치로 재갱신
print(ans)