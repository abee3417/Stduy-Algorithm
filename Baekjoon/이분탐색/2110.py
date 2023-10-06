#이분탐색을 배열의 인덱스가 아닌 거리로 계산하고, mid로 공유기를 왼쪽부터 설치해본다는 아이디어
import sys 
input = sys.stdin.readline

N, C = map(int, input().split())
h = [0 for _ in range(N)]
for i in range(N):
    h[i] = int(input())
h.sort()
left, right = 1, h[-1] - h[0] #방법 : h내에서 가능한 최소 거리와 최대 거리를 일단 설정한다
while (left <= right):
    mid = (left + right) // 2 #루프를 돌면서 mid(중간)값이 되는 거리를 두 공유기의 최단거리로 가정을 하고
    val, cnt = h[0], 1 #h[0]에는 무조건 설치했다고 가정
    for i in range(1, N): #mid만큼 공유기를 설치해본다
        if (h[i] >= val + mid):
            val, cnt = h[i], cnt + 1
    if (cnt < C): #더 적게 설치됐다면 mid가 크다는 의미이므로 mid를 right로 잡아주고
        right = mid - 1
    else: #같거나 더 많이 설치됐다면, mid를 left로 잡아주고
        left = mid + 1
        ans = mid #거리를 좁히면서 더 최적의 결과가 나올 수 있으므로 값을 저장해준다
print(ans)