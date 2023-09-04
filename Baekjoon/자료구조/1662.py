s = list(input())
flag = 0
result = 0
arr = [0 for i in range(50)]
arr.append(0)
while (len(s) != 0):
    tmp = s.pop()
    if (tmp == ')'):
        flag += 1
        arr[flag] = 0
    elif (tmp == '(' and flag > 0):  
        tmp = s.pop()
        arr[flag] *= int(tmp)
        arr[flag - 1] += arr[flag]
        flag -= 1
    else:
        arr[flag] += 1
print(arr[0])