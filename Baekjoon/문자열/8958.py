slist = []
acc = 0
score = 0
cnt = int(input())
for i in range(cnt):
    result = input()
    for i in result:
        if (i == 'O'):
            score += (1 + acc)
            acc += 1
        elif (i == 'X'):
            acc = 0
    slist.append(score)
    acc = 0
    score = 0
for i in slist:
    print(i)