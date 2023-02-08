def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)

n, k = map(int, input().split())
print(fact(n) // (fact(k) * fact(n-k)))