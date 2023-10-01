from itertools import combinations
n, m = map(int, input().split())
home, kfc = [], []
cnt = 0
for y in range(1, n+1):
    li = list(map(int, input().split()))
    for x in range(n):
        if (li[x] == 1): home.append((y, x+1)) #집 좌표 리스트 채우기
        elif (li[x] == 2): #치킨집 좌표 리스트 채우기
            cnt += 1
            kfc.append((y, x+1))
ans = 1000000
for idx in list(combinations([i for i in range(cnt)], m)): #백트래킹을 위한 combination 구하기
    kfc_dis = 0
    for i in home:
        home_y, home_x = i #집 idx
        min_dis = 1000000
        for j in idx:
            kfc_y, kfc_x = kfc[j] #치킨집 idx
            min_dis = min(abs(kfc_y - home_y) + abs(kfc_x - home_x), min_dis) #가장 작은 집 치킨거리 계산
        kfc_dis += min_dis #치킨거리 누적합
    ans = min(kfc_dis, ans) #가장 작은 도시 치킨거리 계산
print(ans)