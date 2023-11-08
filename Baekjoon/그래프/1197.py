#최소 스패닝 트리(MST) 입문 문제 -> 프림 알고리즘 사용
#프림 알고리즘 : heap에 간선 자체의 가중치를 넣어 사용
import sys, heapq
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visit = [0 for _ in range(V+1)] #visit으로 방문하지 않은 점만 탐색하여 MST를 구성할 수 있게끔 한다
q = [] #heapq를 사용해서 간선 수가 v-1개가 될때 까지 가장 저렴한 간선만을 뽑아낸다
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B)) #heapq를 이용하므로 cost를 idx0에 넣는다
    graph[B].append((C, A))
for i in graph[1]: #1번 노드부터 탐색 시작
    heapq.heappush(q, i)
visit[1] = 1
ans, cnt = 0, 0 #ans : MST의 cost, cnt : 지금까지 센 간선 수
while (len(q) != 0):
    if (cnt == V-1): break #MST의 간선 수는 V-1개이다
    cost, node = heapq.heappop(q)
    if (visit[node] == 0): #뽑아낸 노드가 방문하지 않은 거라면
        cnt += 1 #cnt와 ans를 갱신
        ans += cost
        visit[node] = 1
        for i in graph[node]: #다음 탐색할 노드 후보들을 heapq에 삽입
            next_c, next_n = i
            if (visit[next_n] == 0):
                heapq.heappush(q, i)
print(ans)