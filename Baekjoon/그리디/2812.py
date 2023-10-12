#스택+그리디 응용 문제
N, K = map(int, input().split())
n = input()
trash, num = [], [int(n[0])]
cnt = 0
for i in range(1, N):
    tmp = int(n[i])
    if (tmp <= num[-1]): #num의 탑보다 작음 : num에 push
        num.append(tmp)
    else: #num의 탑보다 큼 : 잔여횟수만큼 기존 num의 top을 trash로 옮기고 num에 push
        while num and cnt < K:
            if (tmp <= num[-1]): break
            trash.append(num.pop())
            cnt += 1
        num.append(tmp)
for i in range(cnt, K): #초과되는 수는 빼준다
    num.pop()
for i in num:
    print(i, end='')
'''
Ex) n = 775841
t: , n: 4
t: , n: 4 1
t: 1 4, n: 7
t: 1 4, n: 7 7
t: 1 4, n: 7 7 2
t: 1 4 2, n: 7 7 5
t: 1 4 2, n: 7 7 5 2
t: 1 4 2 2, n: 7 7 5 8
t: 1 4 2 2, n: 7 7 5 8 4
t: 1 4 2 2, n: 7 7 5 8 4 1
'''