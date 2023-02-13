import sys
n = int(input())
# 우선 리스트들의 기본 rank를 1로 해준다.
rank = [1 for i in range(n)]
li = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    li.append([x, y])
# 리스트의 요소들보다 작으면 rank를 하나씩 뒤로해준다.
for i in range(n):
    for j in range(n):
        if (li[i][0] < li[j][0] and li[i][1] < li[j][1]):
            rank[i] += 1
print(' '.join(str(s) for s in rank))