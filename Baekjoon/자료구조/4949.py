li = []
result = []
judg = True
while True:
    s = input()
    if (s == '.'):
        break
    for i in range(len(s)):
        if ((s[i] == ')' or s[i] == ']') and len(li) == 0):
            judg = False
            break
        elif (s[i] == '(' or s[i] == '['): 
            li.append(s[i])
        elif (s[i] == ')'):
            test = li.pop()
            if (test == '['):
                judg = False
                break
        elif (s[i] == ']'):
            test = li.pop()
            if (test == '('):
                judg = False
                break
    if (len(li) == 0 and judg == True):
        result.append('yes')
    else:
        result.append('no')
    li = []
    judg = True
for i in result:
    print(i)