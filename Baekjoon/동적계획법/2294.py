#동전1(2293)과 다른 문제 : 사용된 동전의 최소 갯수 구하기
#그래서 dp테이블에는 i원을 만들 때 가장 적개 사용된 갯수를 저장한다
n, k = map(int, input().split())
val = [] #중복제거
dp = [1000000 for i in range(k+1)]
dp[0] = 0
for _ in range(n):
    val.append(int(input()))
val = sorted(set(val))
for i in range(1, k+1): #첫 dp테이블 초기화
    if (i%val[0] == 0):
        dp[i] = i // val[0]
for i in range(1, len(val)):
    coin = val[i]
    for j in range(i, k+1):
        if (j-coin >= 0):
            dp[j] = min(dp[j], dp[j-coin] + 1)
if (dp[k] == 1000000): print(-1)
else: print(dp[k])