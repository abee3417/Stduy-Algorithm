import copy

def direct(y, x, n, w): #방향에 따른 좌표반환함수, w는 가중치
    match n:
        case 1 : return (y-w, x)
        case 2 : return (y-w, x-w)
        case 3 : return (y, x-w)
        case 4 : return (y+w, x-w)
        case 5 : return (y+w, x)
        case 6 : return (y+w, x+w)
        case 7 : return (y, x+w)
        case 8 : return (y-w, x+w)

def find(fish, idx): #물고기 좌표를 찾아주는 함수
    for y in range(4):
        for x in range(4):
            if (fish[y][x][0] == idx):
                return y, x
    return False

def shark(y, x, eat, fish): #상어 갱신 함수
    global ans
    eat += fish[y][x][0]
    ans = max(ans, eat) #점수 합산
    fish[y][x][0] = 0 #상어 좌표에 상어 투입 (빈칸도 퉁침)
    for idx in range(1, 17): #물고기 이동 시작
        if (find(fish, idx) == False): continue
        while True: #물고기 이동 작업
            sp_y, sp_x = find(fish, idx) #현재 물고기의 정보
            sp_way = fish[sp_y][sp_x][1]
            rp_y, rp_x = direct(sp_y, sp_x, sp_way, 1)
            if (0 <= rp_y <= 3 and 0 <= rp_x <= 3):
                if not (rp_y == y and rp_x == x): #빈칸or상어가 아닐 때만 교환
                    fish[sp_y][sp_x], fish[rp_y][rp_x] = fish[rp_y][rp_x], fish[sp_y][sp_x] #실제위치 교환
                    break
            if (fish[sp_y][sp_x][1] < 8): #현재 물고기 방향변경
                fish[sp_y][sp_x][1] += 1
            else:
                fish[sp_y][sp_x][1] = 1
    for i in range(1, 4):
        new_y, new_x = direct(y, x, fish[y][x][1], i)
        if (0 <= new_y <= 3 and 0 <= new_x <= 3 and fish[new_y][new_x][0] > 0):
            shark(new_y, new_x, eat, copy.deepcopy(fish))

f = [[] for _ in range(4)]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        f[i].append([tmp[j], tmp[j+1]])
ans = 0
shark(0, 0, 0, f) #상어이동시작
print(ans)