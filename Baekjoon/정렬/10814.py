import sys

n = int(input())
result = []
for i in range(n):
    age, name = sys.stdin.readline().strip('\n').split()
    result.append((age, name))
result.sort(key = lambda x : int(x[0]))
for i in result:
    print(str(i[0]) + ' ' + str(i[1]))