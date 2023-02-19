import sys
stack = []
k = int(input())
for i in range(k):
    num = int(sys.stdin.readline().strip('\n'))
    if (num == 0):
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))