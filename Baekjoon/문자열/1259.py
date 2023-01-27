result = []
judg = ''
while True:
    n = input()
    if (n == '0'):
        break
    for i in range(len(n)//2):
        if (n[i] == n[len(n)-1-i]):
            continue
        else:
            judg = 'no'
            break
    if (judg != 'no'):
        judg = 'yes'
    result.append(judg)
    judg = ''
for i in result:
    print(i)