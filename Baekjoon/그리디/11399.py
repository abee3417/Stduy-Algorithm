n = int(input())
li = list(map(int, input().split()))
sum = 0
pre = 0
for i in sorted(li):
    sum += pre + i
    pre += i
print(sum)
