import sys
land = [] # 블록 현황을 담는 리스트
result = {} # 결과를 담는 리스트
n, m, b = map(int, sys.stdin.readline().rstrip().split())
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    land.append(tmp)
# 경우의 수마다 모두 땅고르기 작업을 진행
for i in range(257):
    low, high = 0, 0
    for y in land:
        for x in y:
            if (x > i): # 더 높은 경우 : 부수는 블록갯수
                high += (x - i)
            else: # 더 낮은 경우 : 채우는 블록 갯수
                low += (i - x)
    # 채워야 하는 블록 수보다 (부수는 블록+기존 블록) 수가 많아야 평평하게 할 수 있다.
    if (high + b >= low):
        time = (high * 2) + low
        result[time] = i

val = min(result.keys())
print(val, end=' ')
print(result.get(val))