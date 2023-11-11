import sys
sys.setrecursionlimit(10**6)

def dfs(cur, w):
    global ans
    if (len(tree[cur]) == 0):
        return w
    val, max1, max2 = 0, 0, 0
    for i in tree[cur]:
        val = dfs(i[0], i[1]) #i[0] : 자식노드의 숫자정보, i[1] : 간선의 cost
        tmp = max(max1, val)
        if (tmp == val): #최대값 1,2등 갱신
            max2 = max1
            max1 = tmp
        elif (val > max2): #최대값 2등 갱신
            max2 = val
    if (max1 + max2 > ans): #지름(ㅅ)이 만들어지면, 기존의 지름 최대값과 비교해준다
        ans = max1 + max2
    return w + max1

ans = 0
n = int(input())
tree = [[] for _ in range(n+1)] #자식의 노드정보와 간선의 cost 2가지를 저장하기 위함
for _ in range(n-1):
    parent, child, weigh = map(int, sys.stdin.readline().rstrip().split())
    tree[parent].append((child, weigh)) #단방향으로만 탐색해도 되므로 append는 부모-자식만
dfs(1, 0)
print(ans)