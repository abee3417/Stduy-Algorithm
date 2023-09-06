import sys
n = int(input())
li1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
li2 = list(map(int, sys.stdin.readline().rstrip().split()))
li1.sort()
dic = {}

for i in li1:
    if (i in dic):
        dic[i] += 1
    else:
        dic[i] = 1

for i in li2:
    if (i in dic):
        print(dic[i], end=" ")
    else:
        print(0, end=" ")