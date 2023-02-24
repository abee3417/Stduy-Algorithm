n, m = map(int, input().split())
li = []
result = []
for i in range(n):
    li.append(list(input()))
for i in range(n-7):
    for j in range(m-7):
        prior = li[i][j]
        sum_caseB = 0
        sum_caseW = 0
        for y in range(8):
            for x in range(8):
                cur = li[i+y][j+x]
                # 짝수 인덱스 칸 [0][0], [1][3], [2][2] 등
                if ((x+y) % 2 == 0):
                    # 왼쪽 맨 위가 각각 B와 W일 경우로 나누고 맞지 않은 알파벳이 오면 해당 케이스의 sum을 +1
                    if (cur != 'B'):
                        sum_caseB += 1
                    if (cur != 'W'):
                        sum_caseW += 1
                # 홀수 인덱스 칸 [0][1], [3][0], [1][2] 등
                else:
                    if (cur != 'B'):
                        sum_caseW += 1
                    if (cur != 'W'):
                        sum_caseB += 1
        result.append(min(sum_caseB, sum_caseW)) # 덜 고친 케이스를 결과리스트에 append
print(min(result))
