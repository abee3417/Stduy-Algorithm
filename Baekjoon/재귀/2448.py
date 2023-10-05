import sys

def star(n):
    if (n == 3):
        return ["  *   ", " * *  ", "***** "]
    base = star(n//2)
    new = [" " * (n*2) for _ in range(n)] #새로운 패턴(base) 만들어서 리턴하기 위함
    for i in range(n//2): #윗삼각형 정의
        new[i] = new[i][:n//2] + base[i] + new[i][n//2+n:]
    for i in range(n//2, n): #아래 2개 삼각형 정의
        tmp = base[i-(n//2)] * 2
        new[i] = new[i].replace(new[i], tmp)
    return new

n = int(input())
result = "\n".join(star(n))
for i in result:
    sys.stdout.write(i)