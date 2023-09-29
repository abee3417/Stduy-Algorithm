#min-heap(priority-q)응용문제
import sys, heapq
heap = []
n = int(input())
time = []
for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    time.append([n1, n2])
time.sort(key=lambda x : (x[0], x[1])) #어차피 종료시간은 min-heap에 의해 알아서 정렬되므로 시작시간 기준 정렬
heapq.heappush(heap, time[0][1])
for i in range(1, n):
    start = time[i][0]
    if (start >= heap[0]): #뒷시간에 붙일 수 있다면, heap의 root를 pop하고 새로 push
        heapq.heappop(heap)
        heapq.heappush(heap, time[i][1])
    else: #없다면 강의실 추가
        heapq.heappush(heap, time[i][1])
print(len(heap))