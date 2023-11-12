s1 = " " + input()
s2 = " " + input()
l1 = len(s1)
l2 = len(s2)
dp = [[0 for _ in range(l2)] for _ in range(l1)]
for i in range(1, l1):
    for j in range(1, l2):
        if (s1[i] == s2[j]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[l1-1][l2-1])