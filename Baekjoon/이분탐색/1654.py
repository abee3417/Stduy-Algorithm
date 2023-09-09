import sys
li = []
k, n = map(int, sys.stdin.readline().strip('\n').split())
for i in range(k):
    li.append(int(sys.stdin.readline().rstrip()))
li = sorted(li)
left = 1
max = 0
right = li[-1]
while (left <= right):
    result = 0
    if (li[0] == li[-1]):
        mid = right
    else:
        mid = (left + right) // 2
    for i in range(k):
        result += li[i] // mid
    if (result < n):
        right = mid - 1
    elif (max < mid):
        max = mid
        left = mid + 1
print(max)