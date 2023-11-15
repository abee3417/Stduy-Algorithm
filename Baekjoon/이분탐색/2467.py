#이분탐색+두포인터
N = int(input())
liq = list(map(int, input().split()))
l, r = 0, -1
std = 2000000001
ans = [liq[l], liq[r]]
while (liq[l] < liq[r]):
    if (abs(liq[l]+liq[r]) <= std):
        std = abs(liq[l]+liq[r])
        ans = [liq[l], liq[r]]
    if (liq[l]+liq[r] > 0): r -= 1
    else: l += 1
print(ans[0], ans[1])