# bfs로 트리를 만들면서, level에 따른 정답 출력을 의도
from collections import deque
q = deque()
visit = [0 for _ in range(200002)]
n, k = map(int, input().split())
if (n == k): print(0)
else:
    if (n == 0): child_node = 1 # 첫 child node수 설정
    elif (n == 1) : child_node = 2
    else: child_node = 3
    search_t = -1
    level = 1
    q.append(n)
    visit[n] = 1
    while True: # bfs start
        cur = q.popleft()
        search_t += 1
        if (cur == k): break
        move = [-1, 1, cur]
        for i in range(3):
            next = cur + move[i]
            if (next > 200000 or next < 0): continue
            if (visit[next] == 0):
                q.append(next)
                visit[next] = 1
        if (search_t == child_node): # 조건 만족 시 level, 다음 level을 위한 목표 child node수 초기화
            level += 1
            search_t = 0
            child_node = len(q)
    print(level)