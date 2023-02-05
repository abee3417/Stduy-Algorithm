# 에라토스테네스의 체를 이용하면 빠르게 구할 수 있다.
'''
1제거
이후 math.sqrt(n)까지의 소수들에 한해
소수 자체를 제외한 소수의 배수들을 모두 제거한다.
예) 100까지의 소수면 2,3,5,7의 배수들을 제거
'''
import math

m, n = map(int, input().split())
p = [1] * (n + 1) # 아래 반복문에서 소수가 아닌건 0으로 바꾸며 지울 것이다.
p[0], p[1] = 0, 0
for i in range(2, int(math.sqrt(n))+1):
    if (p[i] != 0): # 이미 지워진 수는 볼 필요가 없다.
        index = i * 2
        while (index <= n):
            p[index] = 0
            index += i
for i in range(m, n+1):
    if (p[i] == 1):
        print(i)