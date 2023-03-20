from collections import deque
n, m = map(int, input().split())
q = deque()
for i in range(1, n+1):
    q.append(i)
li = list(map(int, input().split()))
cnt = 0
for i in li:
    if (q.index(i) <= n//2):
        while True:
            if (q[0] == i):
                q.popleft()
                n -= 1
                break
            else:
                q.append(q.popleft())
                cnt += 1
    else:
        while True:
            if (q[0] == i):
                q.popleft()
                n -= 1
                break
            else:
                q.appendleft(q.pop())
                cnt += 1
print(cnt)