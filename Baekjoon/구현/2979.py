a, b, c = map(int, input().split())
result = 0
time = [0] * 101
for i in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        time[j] += 1
for i in time:
    if (i == 0):
        continue
    elif (i == 1):
        result += a
    elif (i == 2):
        result += b * 2
    elif (i == 3):
        result += c * 3
print(result)