stack, count = [], 0
s = input()
for i in range(len(s)):
    if (s[i] == '('):
        stack.append(s[i])
        count += 1
    elif (s[i] == ')'):
        # 레이저일 경우 막대갯수를 원상태로 복구 후 count 갱신
        if (s[i-1] == '('):
            stack.pop()    
            count -= 1
            count += len(stack)
        else:
            stack.pop()
print(count)