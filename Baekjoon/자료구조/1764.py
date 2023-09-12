import sys
n, m = input().split()
n = int(n)
m = int(m)
not_listen = {}
cnt = 0
result = []
for i in range(n):
    not_listen[sys.stdin.readline().rstrip()] = i
for i in range(m):
    try:
        test = sys.stdin.readline().rstrip()
        not_listen[test]
        result.append(test)
        cnt += 1
    except:
        continue
print(cnt)
result = sorted(result)
for i in result:
    print(i)