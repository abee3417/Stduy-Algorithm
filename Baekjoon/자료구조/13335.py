import sys
from collections import deque
n, w, l = map(int, sys.stdin.readline().strip('\n').split())
li = list(map(int, input().split()))
arr_len = len(li)
pos = [0 for i in range(arr_len)]
bridge = deque()
flag = True
result = 0
start = 0
end = 0
while True:
    cur_len = len(bridge)
    cur_ton = sum(bridge)    
    for i in range(end, start): #위치정보갱신
        pos[i] += 1
        if (pos[i] > w):
            bridge.popleft()
            end += 1
    if (start < n):
        if (cur_len+1 <= w and cur_ton+li[start] <= l):
            bridge.append(li[start])
            pos[start] += 1
            start += 1
    if (pos[arr_len-1] > w): #마지막 트럭까지 모두 지나면 break
        #result -= 1
        break
    result += 1
print(result)