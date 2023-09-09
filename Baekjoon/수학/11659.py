#누적합배열
import sys
n, m = input().split()
n = int(n)
m = int(m) 
li = list(map(int, input().split()))
cumsum = [0 for x in range(n+1)]
for x in range(n):
    cumsum[x+1] = cumsum[x] + li[x]
for x in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(cumsum[j] - cumsum[i-1])

