s = input()
stack = []
priority = {'(':0, '+':1, '-':1, '*':2, '/':2}
for i in s:
    if ('A' <= i <= 'Z'): print(i, end='')  
    elif (i == '(' or len(stack) == 0):
        stack.append(i)
    elif (i == ')'):
        while True:
            top = stack.pop()
            if (top == '('): break
            print(top, end='')
    else: #stack의 맨 위의 연산자 우선순위가 낮아야만 한다 (ex. *위에 -가 오면 안됨)
        while (len(stack) != 0 and priority[stack[-1]] >= priority[i]):
            top = stack.pop()
            print(top, end='')
        stack.append(i)
while (len(stack) != 0):
    print(stack.pop(), end='')