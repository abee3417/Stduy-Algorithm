import sys
from collections import deque

def _round(n):
    return round(n + 10**(-len(str(n))-1))

li = []
n = int(input())
if (n == 0):
    print("0")
else:
    for i in range(n):
        li.append(int(sys.stdin.readline().rstrip()))
    li = deque(sorted(li))
    del_n = int(_round(n * (15/100)))
    for i in range(del_n):
        li.pop()
        li.popleft()
        n -= 2
    print(int(_round(sum(li)/n)))