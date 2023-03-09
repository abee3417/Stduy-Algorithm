import sys
S = []

def push(n):
    S.append(n)

def pop():
    if (len(S) == 0):
        print(-1)
    else:
        print(S.pop())

def size():
    print(len(S))

def empty():
    if (len(S) == 0):
        print(1)
    else:
        print(0)

def top():
    if (len(S) == 0):
        print(-1)
    else:
        print(S[-1])
    
num = int(input())
for i in range(num):
    s = sys.stdin.readline().rstrip()
    if (s != 'pop' and s != 'size'
        and s != 'empty' and s != 'top'):
        s, n = map(str, s.split())

    if (s == 'push'):
        push(n)
    elif (s == 'pop'):
        pop()
    elif (s == 'size'):
        size()
    elif (s == 'empty'):
        empty()
    elif (s == 'top'):
        top()