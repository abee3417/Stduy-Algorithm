n = int(input())
cnt = 0
while True:
    if (n%5 == 0 or n < 3):
        break
    n -= 3
    cnt += 1
if (n%5 == 0):
    cnt += n // 5
else:
    cnt = -1
print(cnt)