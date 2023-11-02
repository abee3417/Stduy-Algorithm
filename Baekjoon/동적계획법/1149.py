n = int(input())
ans = 0
info = [[] for _ in range(n+1)]
price = [[0, 0, 0] for _ in range(n+1)] #info와 동일한 크기의 dp용 기록테이블, 해당 idx까지의 최소값을 기록
for i in range(1, n+1):
    info[i] = list(map(int, input().split()))
price[1] = info[1]
for i in range(2, n+1): #idx 2값과 idx-1 위치의 2개값 중 더 작은값을 더해준걸 테이블에 기록
    price[i][0] = info[i][0] + min(price[i-1][1], price[i-1][2])
    price[i][1] = info[i][1] + min(price[i-1][0], price[i-1][2])
    price[i][2] = info[i][2] + min(price[i-1][0], price[i-1][1])
print(min(price[n]))