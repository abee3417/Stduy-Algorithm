import sys
n = int(input())
result = 0
for i in range(n):
    s = sys.stdin.readline().rstrip()
    # 문자열 길이가 홀수면 좋은단어 X
    if(len(s) % 2 == 0):
        stack = []
        for i in s:
            if (len(stack) == 0):
                stack.append(i)
            elif (stack[-1] == i):
                stack.pop()
            else:
                stack.append(i)
        if (len(stack) == 0):
            result += 1
print(result)
