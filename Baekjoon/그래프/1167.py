#1967과 동일하나 dfs를 2번 사용하는 코드로 변경
import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    global visit
    for i in tree[cur]:
        next, w = i[0], i[1]
        if (visit[next] == 0):
            visit[next] = visit[cur] + w
            dfs(next)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(1, len(tmp)-1, 2):
        tree[tmp[0]].append((tmp[i], tmp[i+1]))
visit = [0 for _ in range(n+1)]
dfs(1) #일단 1에서 첫번째 dfs 시작
max_idx = visit.index(max(visit)) #가장 값이 큰(멀리 떨어진) 노드의 idx 추출
visit[1] = 0 #시작점은 0으로 초기화
visit = [0 for _ in range(n+1)]
dfs(max_idx)
visit[max_idx] = 0 #시작점은 0으로 초기화
print(max(visit)) #max_idx에서 가장 멀리 떨어진 곳과의 w를 print