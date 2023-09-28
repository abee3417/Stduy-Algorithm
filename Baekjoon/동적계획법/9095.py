T = int(input())
memo = [0 for i in range(11)]
memo[1] = 1 #1
memo[2] = 2 #1+1, 2
memo[3] = 4 #1+1+1, 1+2, 2+1, 3
for i in range(4, 11):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
for i in range(T):
    n = int(input())
    print(memo[n])

    
