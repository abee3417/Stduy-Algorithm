n = int(input())
round, min = 1, 2
while True:
    if (n < min):
        break
    else:
        min += round * 6
        round += 1
print(round)