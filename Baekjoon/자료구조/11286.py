# heapq 라이브러리를 사용한 방법
import sys
import heapq
heap = []

n = int(input())
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if (x != 0):
        heapq.heappush(heap, (abs(x), x))
    elif (x == 0 and len(heap) == 0):
        print(0)
    else:
        print(heapq.heappop(heap)[1]) #원래값 출력