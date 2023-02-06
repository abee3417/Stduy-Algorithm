s = input()
result = []
for i in s:
    n = ord(i)
    if (65 <= n <= 77 or 97 <= n <= 109):
        result.append(chr(n+13))
    elif (78 <= n <= 90 or 110 <= n <= 122):
        result.append(chr(n-13))
    else:
        result.append(i)
print(''.join(result))