N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))
gap = []
for i in range(1, N):
    gap.append(sensor[i] - sensor[i-1])
gap.sort(reverse=True)
print(sum(gap[(K-1):]))