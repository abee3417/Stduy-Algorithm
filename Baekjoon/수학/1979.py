import math
def isPrime(n):
    if (n < 2):
        return False
    if (n == 2 or n == 3):
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

n = int(input())
li = list(map(int, input().split()))
cnt = 0
for i in li:
    if (isPrime(i) == True):
        cnt += 1
print(cnt)