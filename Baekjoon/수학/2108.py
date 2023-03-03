import sys
min_done, max_done, cnt_done = False, False, False
sum, cnt, freq_max = 0, -1, 0
freq_val = []
index_list = [0 for i in range(8001)]
n = int(input())

# 반복하면서 통계값을 계산
for i in range(n):
    num = int(sys.stdin.readline().strip('\n'))
    index_list[num+4000] += 1
    sum += num
for i in range(8001):
    # 중앙값 계산
    if (index_list[i] > 0 and cnt_done == False):
        cnt += index_list[i]
        if (cnt >= n//2):
            cnt_done = True
            cnt = i-4000
    # 최빈값 계산
    if (freq_max < index_list[i]):
        freq_max = index_list[i]
        freq_val = []
        freq_val.append(i-4000)
    elif (freq_max == index_list[i]):
        freq_val.append(i-4000)
    # 범위 계산
    if (index_list[i] > 0 and min_done == False):
        min = i - 4000
        min_done = True
    if (index_list[8000-i] > 0 and max_done == False):
        max = 4000 - i
        max_done = True

# 최빈값에서 2번째로 작은값 찾기
if (len(freq_val) <= 1):
    freq_val = freq_val[0]
else:
    freq_val = sorted(freq_val)[1]

# 평균값 조정하기
avg = sum//n
avg_real = sum/n - avg
if (avg_real >= 0.5):
    avg += 1
# 통계값 4개 출력하기
print(avg)
print(cnt)
print(freq_val)
print(max-min)
