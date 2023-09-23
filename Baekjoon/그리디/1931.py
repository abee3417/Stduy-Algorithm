import sys
n = int(input())
time = []
cnt = 1
for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    time.append([n1, n2])
time.sort(key=lambda x : (x[1], x[0]))
end = time[0][1]
for i in range(1, n):
    start = time[i][0]
    if (start >= end):
        cnt += 1
        end = time[i][1]
print(cnt)