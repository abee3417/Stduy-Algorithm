import copy
result = []
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    before = [0 for i in range(n)]
    after = [0 for i in range(n)]
    sum = 0
    # 0층 셋팅
    for j in range(n):
        before[j] = j+1
    # 1~k층 셋팅
    for x in range(k):
        for y in range(n):
            for z in range(y+1):
                sum += before[z]
            after[y] = sum
            sum = 0
        before = copy.deepcopy(after) # 깊은복사를 해야한다.
    result.append(before[n-1])
for i in result:
    print(i)