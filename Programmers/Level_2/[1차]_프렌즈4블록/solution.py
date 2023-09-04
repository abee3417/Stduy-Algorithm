def solution(m, n, board):
    for i in range(0, m):
        board[i] = list(board[i])
    answer = 0
    while True:
        ans_sheet = [[0 for i in range(0, n)] for i in range(0, m)]
        ans_tmp = 0
        for i in range(0, m-1):
            for j in range(0, n-1): 
                if (board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1] and 'A' <= board[i][j] <= 'Z'):
                    ans_sheet[i][j] = 1
                    ans_sheet[i][j+1] = 1
                    ans_sheet[i+1][j] = 1
                    ans_sheet[i+1][j+1] = 1
        for i in range(0, m):
            for j in range(0, n): 
                if (ans_sheet[i][j] == 1):
                    ans_tmp += 1
                    if (i != 0):
                        for k in range(i, 0, -1):
                            board[k][j] = board[k-1][j]
                            board[k-1][j] = '0'
        if (ans_tmp == 0):
            break
        else:
            answer += ans_tmp
    return answer