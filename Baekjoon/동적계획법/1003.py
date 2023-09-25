T = int(input())
result = [[0, 0] for i in range(41)]
result[0][0] = result[1][1] = 1
for i in range(T):
    n = int(input())
    if (n >= 2):
        for i in range(2, n+1):
            result[i][0] = result[i-1][0] + result[i-2][0]
            result[i][1] = result[i-1][1] + result[i-2][1]
    print(str(result[n][0]) + " " + str(result[n][1]))