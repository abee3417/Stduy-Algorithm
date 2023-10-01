#문제 12904번에서 로직이 변경되었기에 재귀로 변경
import sys
sys.setrecursionlimit(10**6)

ans = 0
def check(test, l):
    global ans
    if (l == len(s)):
        if (test == s): ans = 1
    else:
        if (test[-1] == 'A'):
            check(test[:(l-1)], l-1)
        if (test[0] == 'B'):
            check(test[::-1][:(l-1)], l-1)

s = input()
t = input()
check(t, len(t))
print(ans)