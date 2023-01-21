import sys
result = 0
n = list(map(int, sys.stdin.readline().strip('\n').split()))
for i in n:
    result += i ** 2
print(result % 10)