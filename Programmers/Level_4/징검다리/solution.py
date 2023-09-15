def solution(distance, rocks, n):
    rocks.sort()
    start = 0
    answer = 0
    end = distance
    rocks.append(distance)
    while (start <= end): # mid를 정답으로 가정
        mid = (start + end) // 2
        pre = 0 # 이전 자리
        remv_cnt = 0 # 제거한 바위 수
        for i in rocks:
            if (i - pre < mid): # 최소거리 내에는 바위가 없어야하므로 거리가 작으면 바위를 제거
                remv_cnt += 1
            else: # 거리 만족하면 이전 자리를 갱신하여 다시 탐색
                pre = i
        # 제거 바위가 너무 많으면 끝점을 줄인다
        if (remv_cnt > n):
            end = mid - 1
        # 아니면 적절범위므로 max찾고 시작점을 늘린다
        else:
            answer = max(answer, mid)
            start = mid + 1
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))