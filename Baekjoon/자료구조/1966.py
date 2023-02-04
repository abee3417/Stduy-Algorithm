from collections import deque
import sys
result = []
case = int(input())
for i in range(case):
    n, m = map(int, sys.stdin.readline().strip('\n').split())
    q = deque(sys.stdin.readline().strip('\n').split())
    target = m
    count = 0
    _max = max(q)
    while True:
        if (_max == q[0]): # 맨 앞이 가장 클 경우
            count += 1
            n -= 1 # q의 사이즈도 하나 줄어들게 한다.
            if (target == 0):
                result.append(count)
                break
            else:
                target -= 1
                q.popleft()
                _max = max(q) # max값을 다시 갱신
        else: # 나머지
            q.append(q.popleft())
            if (target == 0):
                target = n - 1 # target이 맨 앞이면 인덱스를 맨 뒤로 변경
            else:
                target -= 1
for i in result:
    print(i)
        