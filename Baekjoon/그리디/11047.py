n, k = map(int, input().split())
li = []
result = 0
for i in range(n):
    tmp = int(input())
    if (tmp <= k):
        li.append(tmp)
li.sort(reverse=True)
for i in li:
    tmp = k // i
    k -= i * tmp
    result += tmp
print(result)