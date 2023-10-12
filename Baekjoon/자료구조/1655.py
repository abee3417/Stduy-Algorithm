'''
#시간초과가 나는 기존코드
import sys, heapq
input = sys.stdin.readline
N = int(input())
li = []
for i in range(N):
    li.append(int(input()))
    li.sort()
    tmp = list(li[i//2:])
    heapq.heapify(tmp)
    print(heapq.heappop(tmp))
'''
import sys, heapq
input = sys.stdin.readline
N = int(input())
n = int(input())
min_h, max_h = [], [] #min heap, max heap을 이용해서 time cost를 최소화하면서 중앙값을 찾는 알고리즘
mid = n #최초의 중앙값
print(mid) 
for i in range(1, N):
    n = int(input())
    # ex) mid = 5일 시 max : [-4(4), -3(3), -2(2), -1(1)], min : [6, 7, 8, 9] 이런식
    # 오직 max_h에서 가장 큰값(작은값), min_h에서 가장 작은값만 가지고 mid를 판별하기 때문에 heapq를 사용해도 된다
    if (n < mid): #n이 mid보다 작으면 max_h에 push
        heapq.heappush(max_h, -n)
    else: #반대면 min_h에 push
        heapq.heappush(min_h, n)
    if (len(max_h)-len(min_h) >= 1): #mid보다 작은쪽이 큰쪽보다 1 길어지면 mid 재갱신
        heapq.heappush(min_h, mid)
        mid = -heapq.heappop(max_h)
    elif (len(min_h)-len(max_h) >= 2): #mid보다 큰쪽이 작은쪽보다 2 길어지면 mid 재갱신
        heapq.heappush(max_h, -mid)
        mid = heapq.heappop(min_h)
    print(mid)