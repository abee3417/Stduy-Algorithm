import sys
paper = []
result = [0, 0]

def divide(n, arr):
    if (n == 1): #길이1되면 종료
        result[arr[0][0]] += 1
    elif (sum(row.count(0) for row in arr) == n**2): #처음부터 0으로 같을 시
        result[0] += 1
    elif (sum(row.count(1) for row in arr) == n**2): #처음부터 1로 같을 시
        result[1] += 1
    else: #4등분하여 체크하기
        test = []
        test.append([[arr[y][x] for x in range(0, n//2)] for y in range(0, n//2)])
        test.append([[arr[y][x] for x in range(n//2, n)] for y in range(0, n//2)])
        test.append([[arr[y][x] for x in range(0, n//2)] for y in range(n//2, n)])
        test.append([[arr[y][x] for x in range(n//2, n)] for y in range(n//2, n)])
        for i in test:
            flag = False
            for j in range(2):
                tmp = [j for x in range(n//2)]
                if (i.count(tmp) == n//2):
                    result[j] += 1
                    flag = True
                    break
            if (flag == False):
                divide(n//2, i)

n = int(input())
for i in range(n):
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    paper.append(li)
divide(n, paper)
print(result[0])
print(result[1])