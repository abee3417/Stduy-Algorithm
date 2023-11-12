import sys
n, m = map(int, input().split())
table = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    table[i][1:] = list(map(int, sys.stdin.readline().rstrip().split()))
for x in range(1, n+1): #(1,1)부터 (x,y)까지의 누적합 테이블 만들기
    for y in range(1, n+1):
        dp[x][y] = table[x][y] + dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1]
for _ in range(m): #dp 테이블 기준 (x2,y2) - (x2,y1-1) + (x1-1,y2) - (x1-1,y1-y)
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    tmp = dp[x2][y1-1] + dp[x1-1][y2] - dp[x1-1][y1-1]
    print(dp[x2][y2] - tmp)