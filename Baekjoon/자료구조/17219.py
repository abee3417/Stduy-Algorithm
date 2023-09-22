import sys
n, m = map(int, input().split())
dic = {}
for i in range(n):
    site, pw = map(str, sys.stdin.readline().rstrip().split())
    dic[site] = pw
for i in range(m):
    print(dic[sys.stdin.readline().rstrip()])