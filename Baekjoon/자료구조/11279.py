# 직접 max-heap 구현
import sys
heap = [2**31]
cnt = 0

def re_heap_up():
    i = cnt
    while (i > 0):
        if (heap[i] > heap[i//2]):
            heap[i], heap[i//2] = heap[i//2], heap[i]
            i = i // 2
        else:
            break

def re_heap_down():
    i = 1
    while (i < cnt and 2*i <= cnt):
        if (2*i+1 > cnt): #오른쪽 자식 존재X 경우
            if (heap[i] < heap[2*i]):
                heap[i], heap[2*i] = heap[2*i], heap[i]
                i = i * 2
            else:
                break
        else:
            if (heap[i] < heap[2*i] and heap[i] < heap[2*i+1]): #자식들이 모두 클 경우
                if (heap[2*i] > heap[2*i+1]):
                    heap[i], heap[2*i] = heap[2*i], heap[i]
                    i = i * 2
                else:
                    heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
                    i = i * 2 + 1
            elif (heap[i] < heap[2*i]): #왼쪽 자식만 클 경우
                heap[i], heap[2*i] = heap[2*i], heap[i]
                i = i * 2
            elif (heap[i] < heap[2*i+1]): #오른쪽 자식만 클 경우
                heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
                i = i * 2 + 1
            else:
                break

n = int(input())
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if (x != 0):
        heap.append(x)
        cnt += 1
        re_heap_up()
    elif (x == 0 and cnt == 0):
        print(0)
    else:
        print(heap[1])
        heap[1] = heap[cnt]
        heap.pop()
        cnt -= 1
        re_heap_down()