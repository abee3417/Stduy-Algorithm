#사선 공식(신발끈 공식) 사용
import sys
input = sys.stdin.readline
n = int(input())
x, y = [], []
for _ in range(n):
    inputX, inputY = map(int, input().split())
    x.append(inputX)
    y.append(inputY)
ans = 0
for i in range(n):
    ans += (x[i]*y[(i+1)%n])
for i in range(n):
    ans -= (x[(i+1)%n]*y[i])
print(round((abs(ans))/2, 1))