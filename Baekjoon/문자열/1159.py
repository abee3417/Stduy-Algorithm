import sys
exist = False
result = ''
n = int(input())
name_arr = [0 for i in range(26)]
for i in range(n):
    name = sys.stdin.readline().strip('\n')[0]
    name_arr[ord(name)-97] += 1
for i in range(26):
    if (name_arr[i] >= 5):
        exist = True
        result += chr(i+97)
if (exist == True):
    print(result)
else:
    print('PREDAJA')