n, m = map(int, input().split())
li = list(map(int, input().split()))
result = 0
for a in range(n-2):
    # 시간복잡도를 최소화하기 위해 합이 m과 같아지면 즉시 반복을 중단한다.
    if (result == m):
        break
    for b in range(a+1, n-1):
        if (result == m):
            break
        for c in range(b+1, n):
            sum = li[a] + li[b] + li[c]
            if (m < sum or sum < result):
                continue
            else:
                result = sum
print(result)