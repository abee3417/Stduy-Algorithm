import sys
input = sys.stdin.readline

N = int(input())
li = [0 for _ in range(N+1)]
li[1:] = list(map(int, input().split()))
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    s, e = S, E
    flag = True
    while (s <= e):
        if (dp[s][e] == 1): break
        if (li[s] != li[e]):
            flag = False
            break
        s, e = s+1, e-1
    if (flag == True):
        dp[S][E] = 1
        print(1)
    else: print(0)