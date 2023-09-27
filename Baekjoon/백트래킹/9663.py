def queen(y):
    global ans
    if (y == n): #n개만큼 퀸을 무사히 두었으면 정답+1
        ans += 1
    else:
        for x in range(n):
            flag = True
            chess[y] = x #메모리초과로 인해 1차원 리스트로 표현, (y, x)에 퀸을 둔 것
            for i in range(y): #확인작업 : 대각선or같은 열에 1(퀸)이 있으면 False
                if (chess[i] == chess[y] or abs(chess[y] - chess[i]) == y-i):
                    flag = False
                    break
            if (flag == True): #조건을 만족하면 다음행으로 이동
                queen(y+1)

n = int(input())
ans = 0
chess = [-1 for _ in range(n)]
queen(0)
print(ans)