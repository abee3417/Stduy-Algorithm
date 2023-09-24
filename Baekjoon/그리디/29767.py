from itertools import combinations
from collections import deque
n, k = map(int, input().split())
li = list(map(int, input().split()))
cumsum = deque(0 for i in range(n+1))
for i in range(n):
    cumsum[i+1] = cumsum[i] + li[i]
cumsum.popleft()
cumsum = sorted(cumsum, reverse=True)
print(sum(cumsum[0:k]))