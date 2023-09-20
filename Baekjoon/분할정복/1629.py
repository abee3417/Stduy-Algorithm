import sys
sys.setrecursionlimit(100000)

# 모듈러 : (a * b)mod c = (a mod c * b mod c) mod c
def mod(n1, p, n2):
    if (p == 1):
        return n1 % n2
    else:
        result = mod(n1, p//2, n2)
        if (p%2 == 0):
            return (result * result) % n2
        else:
            return (result * result * n1) % n2

a, b, c = map(int, input().split())
print(mod(a, b, c))