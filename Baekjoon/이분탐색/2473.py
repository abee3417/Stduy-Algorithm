#2467 심화변형문제
N = int(input())
liq = sorted(list(map(int, input().split())))
std = 3000000001
ans = []
for i in range(N-2):
    l, r = i+1, N-1
    while (l < r):
        if (abs(liq[i]+liq[l]+liq[r]) <= std):
            std = abs(liq[i]+liq[l]+liq[r])
            ans = [liq[i], liq[l], liq[r]]
        if (liq[i]+liq[l]+liq[r] > 0): r -= 1
        else: l += 1
for i in sorted(ans):
    print(i, end=' ')