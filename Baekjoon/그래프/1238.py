import sys, heapq
from collections import deque

def search(n):
    dis, q = [INF for _ in range(N+1)], []
    dis[n] = 0 #출발지점 0
    heapq.heappush(q, (dis[n], n))
    while (len(q) != 0):
        c, v = heapq.heappop(q)
        if (dis[v] < c): continue
        for next_c, next_v in graph[v]:
            if (dis[v] + next_c < dis[next_v]):
                dis[next_v] = dis[v] + next_c
                heapq.heappush(q, (dis[next_v], next_v))
    return dis

INF = sys.maxsize
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
for _ in range(M):
    start, end, T = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append((T, end))
#1. X로 가는 시간 구하기
for i in range(1, N+1):
    ans[i] = search(i)[X]
#2. X에서 가는 시간 구하기
for i in range(1, N+1):
    ans[i] += search(X)[i]
print(max(ans))