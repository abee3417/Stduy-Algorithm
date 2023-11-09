import sys
sys.setrecursionlimit(10**6)

def dfs(y, x, case):
    global visit
    visit[case][y][x] = 1
    location = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우
    for i in location:
        _y = y + i[0] #새로운y
        _x = x + i[1] #새로운x
        _c, c = graph[_y][_x], graph[y][x] #기존 색깔, 새로운 색깔
        if (_c != '*' and visit[case][_y][_x] == 0):
            if (case == 0 and _c == c): #정상인
                dfs(_y, _x, case)
            elif (case == 1 and (_c == c or abs(ord(_c)-ord(c)) == 11)): #적록색약:R과G 동일판정
                dfs(_y, _x, case)

n = int(input())
graph = ['*'*(n+2)]
for _ in range(n):
    graph.append('*' + input() + '*')
graph.append('*'*(n+2))
ans1, ans2 = 0, 0
visit = [[[0 for _ in range(n+2)] for _ in range(n+2)] for _ in range(2)] #0:정상인, 1:적록색약
for i in range(1, n+1):
    for j in range(1, n+1):
        if (graph[i][j] != '*' and visit[0][i][j] == 0): #정상인 count
            dfs(i, j, 0)
            ans1 += 1
        if (graph[i][j] != '*' and visit[1][i][j] == 0): #적록색약 count
            dfs(i, j, 1)
            ans2 += 1
print(str(ans1) + " " + str(ans2))