import sys
input = sys.stdin.readline
N, S = map(int, input().split())
li = list(map(int, input().split()))
s, e, ans = 0, 0, 100001 #s, e는 수열의 시작점에 위치한 두 포인터
SUM = 0
if (S <= 1): print(1)
else:
    while (s < N): #sum(li[s:e])를 하면 시간초과가 발생하므로 아래 방법대로 누적합 갱신
        if (SUM >= S): #부분합이 S이상일 경우 길이를 측정하여 최소값 갱신, 범위축소 (s를 +1, SUM에서 li[s]를 제거)
            ans = min(ans, e-s)
            SUM -= li[s]
            s += 1
        else: #그렇지 않으면 범위확장 (e를 +1, SUM에 li[e]를 추가)
            if (e == N): break #e가 범위초과 시 break
            SUM += li[e]
            e += 1
    print(0 if (ans == 100001) else ans)