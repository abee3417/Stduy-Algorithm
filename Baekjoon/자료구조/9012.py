li = []
result = []
judg = True
t = int(input())
for i in range(t):
    s = input()
    for i in range(len(s)):
        if (s[i] == ')' and len(li) == 0):
            judg = False
            break
        elif (s[i] == '('):
            li.append(s[i])
        elif (s[i] == ')'):
            test = li.pop()
    if (len(li) == 0 and judg == True):
        result.append('YES')
    else:
        result.append('NO')
    li = []
    judg = True
for i in result:
    print(i)
