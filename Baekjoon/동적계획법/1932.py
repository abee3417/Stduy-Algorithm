n = int(input())
triangle = []
dp = [[] for _ in range(n)]
for _ in range(n):
    triangle.append(list(map(int, input().split())))
dp[0] = triangle[0]
for i in range(1, n):
    for j in range(i+1):
        if (j == 0): #첫 노드일 경우
            val = dp[i-1][j]
        elif (j == i): #마지막 노드일 경우
            val = dp[i-1][j-1]
        else: #중간 노드일 경우
            val = max(dp[i-1][j], dp[i-1][j-1])
        dp[i].append(triangle[i][j] + val)
print(max(dp[n-1]))