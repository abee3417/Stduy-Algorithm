T = int(input())
for _ in range(T):
    sticker = [[0], [0]]
    n = int(input())
    sticker[0][1:] = list(map(int, input().split()))
    sticker[1][1:] = list(map(int, input().split()))
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]
    for i in range(2, n+1):
        #이전 노드 중 대각선 2개의 합(dp[n][i-1])이 큰지, 아니면 구석탱이 1개(dp[n][i-2])가 더 큰지 비교하는 아이디어에서 시작
        #n은 현재 행이 0일때 1, 1일때 0이여야만 한다. (바로옆 스티커는 못쓰기 때문에 대각선으로 봐줘야한다)
        dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n], dp[1][n]))