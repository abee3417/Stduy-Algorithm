import sys
nlist, stack, result = [], [], []
n = int(input())
push_num = 0
judg = True
for i in range(n):
    nlist.append(int(sys.stdin.readline().strip('\n')))
for i in nlist:
    while (push_num < i):
        push_num += 1
        stack.append(push_num)
        result.append('+')

    if (stack[-1] == i):
        stack.pop()
        result.append('-')
    else:
        judg = False
        break
if (judg == False):
    print('NO')
else:
    print('\n'.join(result))