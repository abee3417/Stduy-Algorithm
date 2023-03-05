import sys
s = set()
m = int(input())

def add(x):
    if (x not in s): s.add(x)

def remove(x):
    if (x in s): s.remove(x)

def check(x):
    if (x in s): print(1)
    else: print(0)

def toggle(x):
    if (x in s): s.remove(x)
    else: s.add(x)

def all():
    s.update([x for x in range(1, 21)])

def empty():
    s.clear()

for i in range(m):
    opr = sys.stdin.readline().rstrip()
    if (opr != 'all' and opr != 'empty'):
        opr, n = map(str, opr.split())
    if (opr == 'add'): add(int(n))
    elif (opr == 'remove'): remove(int(n))
    elif (opr == 'check'): check(int(n))
    elif (opr == 'toggle'): toggle(int(n))
    elif (opr == 'all'): all()
    elif (opr == 'empty'): empty()