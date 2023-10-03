#그래프의 고정관념을 깨준 문제 (무조건 리스트로 서로 연결할 생각, 자식노드를 다르게 판단하는 관점)
from collections import deque
N, M = map(int, input().split())
ladder, snake = {}, {}
visit = [0 for _ in range(101)]
for _ in range(N): #사다리 이어주기
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M): #뱀 이어주기
    u, v = map(int, input().split())
    snake[u] = v
q = deque()
q.append((1, 0)) #idx0 : 보드게임 칸 num, idx1 : 가는데 필요한 주사위 횟수
visit[1] = 1
while q:
    cur, cnt = q.popleft()
    if (cur == 100):
        print(cnt)
        break
    for i in range(1, 7): #주사위로 갈 수 있는 모든 노드들을 자식으로 취급
        if (cur + i > 100): continue
        elif (cur + i in ladder.keys()): #파이썬의 in을 이용하여 cur+i 위치에 사다리가 있는지를 확인
            next = ladder[cur+i]
        elif (cur + i in snake.keys()): #뱀도 마찬가지
            next = snake[cur+i]
        else: #일반적인 다음칸의 경우  
            next = cur+i
        if (visit[next] == 0):
            q.append((next, cnt+1))
            visit[next] = 1