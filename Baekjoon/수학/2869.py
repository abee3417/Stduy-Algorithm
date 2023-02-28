import sys
a, b, v = map(int, input().split())
day = (v-a)//(a-b)
cnt = (v-a)%(a-b)
if (cnt == 0):
    day += 1
else:
    day += 2
print(day)