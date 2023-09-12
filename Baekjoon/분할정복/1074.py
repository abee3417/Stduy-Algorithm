''' 시간초과 재귀코드
def makez(x, y, n):
    global start, r, c
    if (n == 1):
        if (r == y and c == x):
            print(start)
        else:
            start += 1
    else:
        makez(x, y, n//2)
        makez(x+n//2, y, n//2)
        makez(x, y+n//2, n//2)
        makez(x+n//2, y+n//2, n//2)
'''

n, r, c = map(int, input().split())
answer = 0
while True:
    length = 2**n
    len_half = length // 2
    if (length == 1):
        break
    if (r < len_half and c < len_half):
        start = 0
    elif (r < len_half and c >= len_half):
        start = (length**2) // 4
        c -= len_half
    elif (r >= len_half and c < len_half):
        start = (length**2) // 2
        r -= len_half
    else:
        start = (length**2) // 2 + (length**2) // 4
        c -= len_half
        r -= len_half
    answer += start
    n -= 1
print(answer)

