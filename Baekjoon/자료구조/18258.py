import sys
from collections import deque
Q = deque()

def push(n):
    Q.append(n)

def pop():
    if (len(Q) == 0):
        print(-1)
    else:
        print(Q.popleft())

def size():
    print(len(Q))

def empty():
    if (len(Q) == 0):
        print(1)
    else:
        print(0)

def front():
    if (len(Q) == 0):
        print(-1)
    else:
        print(Q[0])

def back():
    if (len(Q) == 0):
        print(-1)
    else:
        print(Q[-1])
    
num = int(input())
for i in range(num):
    s = sys.stdin.readline().rstrip()
    if (s != 'pop' and s != 'size'
        and s != 'empty' and s != 'front' and s != 'back'):
        s, n = map(str, s.split())

    if (s == 'push'):
        push(n)
    elif (s == 'pop'):
        pop()
    elif (s == 'size'):
        size()
    elif (s == 'empty'):
        empty()
    elif (s == 'front'):
        front()
    elif (s == 'back'):
        back()