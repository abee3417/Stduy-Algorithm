import sys, heapq, copy
input = sys.stdin.readline
N = int(input())
arr = [(0, 0) for _ in range(N)]
tmp = list(map(int, input().rstrip().split()))
for i in range(N):
    arr[i] = (tmp[i], i+1)
heap = copy.deepcopy(arr) #기존 배열과 min-heap을 따로 관리해야 쿼리의 mode1작동이 수월해진다
heapq.heapify(heap)
M = int(input())
for _ in range(M):
    q = list(map(int, input().rstrip().split()))
    if (len(q) == 3): #값갱신 (mode1)
        idx, val = q[1], q[2]
        arr[idx-1] = (val, idx)
        heapq.heappush(heap, (val, idx))
    else: #heapq의 top출력 (mode2)
        while True: #mode1로 인해 top값이 실제와 다를 수 있으므로 이를 체크하고 top을 출력한다
            top_val, top_idx = heap[0]
            if (arr[top_idx-1][0] == top_val): break #정상적으로 같으면 break
            heapq.heappop(heap) #다르면 기존 top을 빼버리고 정상적인 값으로 다시 push
            heapq.heappush(heap, (arr[top_idx-1][0], top_idx))
        print(heap[0][1])