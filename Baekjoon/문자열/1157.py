import sys
s1 = sys.stdin.readline().strip('\n').upper()
# sys.stdin.readline()을 해야 시간복잡도가 낮아진다.
s2 = list(set(s1))
# set으로 중복을 없애주며 시간복잡도를 낮춘다.
max = 0
result = '?'
for i in s2:
    if (max < s1.count(i)):
        max = s1.count(i)
        result = i
    elif (max == s1.count(i)):
        result = '?'
print(result)