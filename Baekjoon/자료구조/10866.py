import sys
from collections import deque
Q = deque()

def push_front(n):
    Q.appendleft(n)

def push_back(n):
    Q.append(n)

def pop_front():
    if (len(Q) == 0):
        print(-1)
    else:
        print(Q.popleft())

def pop_back():
    if (len(Q) == 0):
        print(-1)
    else:
        print(Q.pop())

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
    if (s != 'pop_front' and s != 'pop_back' and
        s != 'size' and s != 'empty' and s != 'front' and s != 'back'):
        s, n = map(str, s.split())

    if (s == 'push_front'):
        push_front(n)
    elif (s == 'push_back'):
        push_back(n)
    elif (s == 'pop_front'):
        pop_front()
    elif (s == 'pop_back'):
        pop_back()
    elif (s == 'size'):
        size()
    elif (s == 'empty'):
        empty()
    elif (s == 'front'):
        front()
    elif (s == 'back'):
        back()