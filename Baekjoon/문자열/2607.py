import sys
cnt = 0
n = int(input())
word = input()
for i in range(n-1):
    w1 = list(word)
    w2 = list(sys.stdin.readline().strip('\n'))
    for j in range(len(w2)):
        # w2의 맨 앞을 pop해서 w1에 있는지 체크한다.
        val = w2.pop(0)
        if (val in w1):
            # 있으면 w1에서 val을 없애주고
            w1.remove(val)
        else:
            # 없으면 다시 원래대로 돌려놓는다.
            w2.append(val)
    # AAAB, ABBB 같은 예외처리를 위해 if문을 따로 써준다.
    if (len(w1) == 1 or len(w1) == 0):
        if (len(w2) == 1 or len(w2) == 0):
            cnt += 1
print(cnt)