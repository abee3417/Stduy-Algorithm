def hanoi(n, src, des, aux):
    if (n == 1):
        print(src + " " + des)
    else:
        hanoi(n-1, src, aux, des)
        print(src + " " + des)
        hanoi(n-1, aux, des, src)

n = int(input())
print(2**n - 1)
if (n <= 20):
    hanoi(n, '1', '3', '2')