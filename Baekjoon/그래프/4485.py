import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
round = 1
while True:
    N = int(input())
    if (N == 0): break
    cost = [[0 for _ in range(N)] for _ in range(N)]
    graph = [[[] for _ in range(N)] for _ in range(N)]
    dis = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N): #코스트 입력받기
        cost[i] = list(map(int, input().rstrip().split()))
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for y in range(N): #그래프 채우기
        for x in range(N):
            for m_y, m_x in move:
                if (0 <= y+m_y < N and 0 <= x+m_x < N):
                    graph[y][x].append((cost[y+m_y][x+m_x], y+m_y, x+m_x))
    h = []
    dis[0][0] = cost[0][0]
    heapq.heappush(h, (dis[0][0], 0, 0))
    while (len(h) != 0):
        cur_cost, cur_y, cur_x = heapq.heappop(h)
        if (cur_cost > dis[cur_y][cur_x]): continue
        for next_cost, next_y, next_x in graph[cur_y][cur_x]:
            if (cur_cost + next_cost < dis[next_y][next_x]):
                dis[next_y][next_x] = cur_cost + next_cost
                heapq.heappush(h, (dis[next_y][next_x], next_y, next_x))
    print("Problem {}: {}".format(round, dis[N-1][N-1]))
    round += 1