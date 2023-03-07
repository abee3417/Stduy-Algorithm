import sys
list = []
n = int(input())
for i in range(n):
    list.append(int(sys.stdin.readline().rstrip()))
list.sort()
for i in list:
    print(i)